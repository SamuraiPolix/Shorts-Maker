import csv
import os
import subprocess
import sys
from string import ascii_letters
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import textwrap


def create_image(text, font_path, font_size, max_char_count, image_size, save_path, text_source, text_color):
    if text_color == None:
        text_color = (255, 255, 255, 255)
    save_path += "/verse_images"
    text = fix_fonts(text, font_path)
    # Open a blank image
    img = Image.new('RGBA', image_size, color=(190, 190, 190, 0))

    # Load selected font
    font = ImageFont.truetype(font=f'{font_path}', size=font_size)
    # font_ref = ImageFont.truetype(font='C:/Bots/ShortsMaker/sources/MouldyCheeseRegular-WyMWG.ttf', size=42)

    # Create DrawText object
    draw = ImageDraw.Draw(im=img)

    # Define our text:
    # Calculate the average length of a single character of our font.
    # Note: this takes into account the specific font and font size.
    avg_char_width = sum(font.getbbox(char)[2] for char in ascii_letters) / len(ascii_letters)

    # Translate this average length into a character count
    max_char_count = max(int(img.size[0] * .718 / avg_char_width), max_char_count)

    # Create a wrapped text object using scaled character count
    new_text = textwrap.fill(text=text, width=max_char_count)

    # Draw the shadow text
    shadow_image = Image.new('RGBA', img.size, color=(255, 255, 255, 0))
    shadow_draw = ImageDraw.Draw(im=shadow_image)
    shadow_draw.text(xy=(img.size[0] / 2 - 1, img.size[1] / 2 + 4), text=new_text, font=font, fill=(0, 0, 0, 80), anchor='mm',
              align='center')
    # Add main text to the image
    draw.text(xy=(img.size[0] / 2, img.size[1] / 2), text=new_text, font=font, fill=text_color, anchor='mm',
              align='center')
    # combine shadow and main
    combined = Image.alpha_composite(shadow_image, img)
    # Crop to fit text
    final = combined.crop(combined.getbbox())
    # print(combined.getbbox()[3]-combined.getbbox()[1])

    # check if image of this source (bible reference) exists already
    path_to_check = f"{save_path}/{text_source}.png"
    i = 1
    while os.path.exists(path_to_check):
        path_to_check = f"{save_path}/{text_source}-{i}.png"
        i += 1
    # Save the image
    final.save(f"{path_to_check}")
    # combined.show()
    return f"{path_to_check}", combined.getbbox()[3]-combined.getbbox()[1]


def create_post_images(video_path: str, output_folder):
    video_name = video_path.split("/")
    video_name = video_name[len(video_name)-1].strip(".mp4")
    temp_image =  f"{output_folder}/TEMP_{video_name}.jpg"
    output_image = f"{output_folder}/{video_name}.jpg"
    ffmpeg_command = (f'ffmpeg -ss 00:00:03.00 -i {video_path} -frames:v 1 {temp_image}')

    # Run FFMPEG command
    try:
        subprocess.check_call(ffmpeg_command, shell=True)
    except subprocess.CalledProcessError as e:
        # Handle the exception here
        print(f"An error occurred: {e}")
        sys.exit()

    cut_image(temp_image, output_image)
    os.remove(temp_image)


def cut_image(image_file, output_file):
    # Set desired ratio
    desired_ratio = 1080 / 1080

    if image_file.endswith('.jpg') or image_file.endswith('.jpeg') or image_file.endswith('.png'):
        # Open the image
        img = Image.open(image_file)

        # Get image dimensions
        width, height = img.size
        ratio = width / height

        # Calculate new dimensions
        if ratio > desired_ratio:
            # Image is wider than desired ratio, crop width
            new_width = round(height * desired_ratio)
            new_height = height
        else:
            # Image is taller than desired ratio, crop height
            new_width = width
            new_height = round(width / desired_ratio)

        # Crop the image in the center
        left = (width - new_width) / 2
        top = (height - new_height) / 2
        right = left + new_width
        bottom = top + new_height
        img = img.crop((left, top, right, bottom))

        # Resize the image if necessary
        if img.size != (1080, 1080):
            img = img.resize((1080, 1080))

        # Save the image to output folder
        img.save(output_file)


def fix_fonts(text, font):
    text = text.replace('—', '-')
    # Font "FlowersSunday" can't display '
    if (font.__contains__("FlowersSunday")):
        return text.replace("'", "")
    return text


def add_sheets(video_names: str, output_path: str, customer_name: str, refs: str, verses: str):
    with open(f'{output_path}/{customer_name}.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["File Name", "Reference", "Verse"])
        for i in range(len(video_names)):
            writer.writerow([video_names[i], refs[i], verses[i]])


def rename_videos(video_folder, csv_file):
    with open(csv_file, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            file_name = row['File Name']
            reference = row['Reference']
            verse = row['Verse']
            video_path = f"{video_folder}/{file_name}"
            new_file_name = get_new_file_name(reference)
            # new_video_path = os.path.join(video_folder, new_file_name)
            new_video_path = f"{video_folder}/{new_file_name}"
            try:
                os.rename(video_path, new_video_path)
            except:
                print(f"Could rename '{file_name}' to '{new_file_name}'")
            # print(f"Renamed '{file_name}' to '{new_file_name}'")


def get_new_file_name(reference):
    # Remove any characters that are not allowed in filenames
    new_name: str = reference.replace(':', '_').strip("(ESV)").rstrip()
    new_name = new_name[:100]  # Limit the filename length if needed
    new_name += '.mp4'
    return new_name