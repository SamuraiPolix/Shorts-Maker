import os
from string import ascii_letters
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import textwrap


def create_image(text, font_path, font_size, max_char_count, image_size, save_path, text_source):
    save_path += "/verse_images"
    text = fix_fonts(text, font_path)
    # Open a blank image
    img = Image.new('RGBA', image_size, color=(190, 190, 190, 0))

    # Load selected font
    font = ImageFont.truetype(font=f'{font_path}', size=font_size)

    # Create DrawText object
    draw = ImageDraw.Draw(im=img)

    # Define our text:
    # Calculate the average length of a single character of our font.
    # Note: this takes into account the specific font and font size.
    avg_char_width = sum(font.getsize(char)[0] for char in ascii_letters) / len(ascii_letters)

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
    draw.text(xy=(img.size[0] / 2, img.size[1] / 2), text=new_text, font=font, fill=(255, 255, 255, 255), anchor='mm',
              align='center')
    # combine shadow and main
    combined = Image.alpha_composite(shadow_image, img)

    # check if image of this source (bible reference) exists already
    path_to_check = f"{save_path}/{text_source}.png"
    i = 1
    while os.path.exists(path_to_check):
        path_to_check = f"{save_path}/{text_source}-{i}.png"
        i += 1
    # Save the image
    combined.save(f"{path_to_check}")
    # combined.show()
    return f"{path_to_check}"


def fix_fonts(text, font):
    # Font 6 can't display '
    if (font.__contains__("FlowersSunday")):
        return text.replace("'", "")
    return text