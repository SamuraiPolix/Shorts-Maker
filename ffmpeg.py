import io
import json
import os
import random
import subprocess
import re
import textwrap
import time
from string import ascii_letters
from PIL import Image, ImageDraw, ImageFont, ImageFilter


def create_image(text, font_path, font_size, max_char_count, image_size, save_path, text_source):
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


# TODO: set good positions
# Define the paths and values to everything
# project_dir = os.getcwd()
verse_text_image_path = "E:/Bots/VideoMaker/verse_images"
video_folder = "E:/Bots/VideoMaker/videos"
audio_folder = "E:/Bots/VideoMaker/audio"
output_folder = "E:/Bots/VideoMaker/customers"
json_file = "E:/Bots/VideoMaker/sources/love_data.json"
# font_dir = "C:/Windows/Fonts"
fonts_dir = "E:/Bots/VideoMaker/sources/fonts"
text_source_font = r"C\:/Users/Samurai/AppData/Local/Microsoft/Windows/Fonts/Aloevera-OVoWO.ttf"
image_path = "E:/Bots/VideoMaker/sources/logo.png"
customer_name = "without_logo"
number_of_videos = 100
fonts = ['E:/Bots/VideoMaker/sources/fonts/AdventureScript.ttf', 'E:/Bots/VideoMaker/sources/fonts/AwesomeQuote.ttf', 'E:/Bots/VideoMaker/sources/fonts/BusterDown.ttf', 'E:/Bots/VideoMaker/sources/fonts/CoffeeJellyUmai.ttf', 'E:/Bots/VideoMaker/sources/fonts/CourierprimecodeRegular.ttf', 'E:/Bots/VideoMaker/sources/fonts/EbGaramond08Regular-2mWe.ttf', 'E:/Bots/VideoMaker/sources/fonts/FlowersSunday.otf', 'E:/Bots/VideoMaker/sources/fonts/GreatVibes-Regular.ttf', 'E:/Bots/VideoMaker/sources/fonts/GreenTeaJelly.ttf', 'E:/Bots/VideoMaker/sources/fonts/HeyMarch.ttf', 'E:/Bots/VideoMaker/sources/fonts/Hugamour.ttf', 'E:/Bots/VideoMaker/sources/fonts/LetsCoffee.otf', 'E:/Bots/VideoMaker/sources/fonts/Lightning Script.ttf', 'E:/Bots/VideoMaker/sources/fonts/LikeSlim.ttf', 'E:/Bots/VideoMaker/sources/fonts/LoftygoalsRegular.otf', 'E:/Bots/VideoMaker/sources/fonts/PineappleDays.ttf', 'E:/Bots/VideoMaker/sources/fonts/RecklessBrush.ttf', 'E:/Bots/VideoMaker/sources/fonts/SenjaSantuy.otf', 'E:/Bots/VideoMaker/sources/fonts/SillyHandScriptRegular.otf', 'E:/Bots/VideoMaker/sources/fonts/SunnySpellsBasicRegular.ttf', 'E:/Bots/VideoMaker/sources/fonts/TakeCoffee.ttf', 'E:/Bots/VideoMaker/sources/fonts/WantCoffee.ttf']
fonts_sizes = [100, 60, 100, 100, 70, 75, 65, 90, 110, 80, 73, 50, 90, 80, 75, 52, 120, 80, 80, 87, 50, 65]
fonts_maxcharline = [38, 35, 35, 34, 25, 37, 30, 35, 37, 35, 35, 34, 35, 35, 35, 35, 35, 35, 35, 35, 35, 35]
run_time_average = 0
if number_of_videos > 1:
    start_time_total = time.time()

# Coordinates of logo image and text2 clips
image_y = 1600
text2_y = 1300

with open(f'{json_file}', 'r', encoding='utf-8') as f:
    jsonData = json.load(f)
verses = jsonData['verses']
refs = jsonData['references']

for i in range(number_of_videos):
    start_time = time.time()
    print(f"Creating Video #{i}")
    text_verse = verses[i]
    text_source = refs[i]

    # Get a list of video files in the specified folder
    video_files = [f"{video_folder}/{file}" for file in os.listdir(video_folder) if file.endswith(".mp4")]

    # Choose a random video file from the list
    video_file = random.choice(video_files)
    random_video_num = video_file.split('/')
    random_video_num = random_video_num[len(random_video_num)-1].split('.')
    random_video_num = random_video_num[0]

    # Choose a random font from list
    random_font_num = random.randint(0, len(fonts) - 1)
    selected_font = fonts[random_font_num]

    # Get a list of audio files in the specified folder
    audio_files = [f"{audio_folder}/{file}" for file in os.listdir(audio_folder) if file.endswith(".mp3")]

    # Choose a random video file from the list
    random_audio_num = random.randint(0, len(audio_files) - 1)
    audio_file = audio_files[random_audio_num]

    # Get the video size
    result = subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'stream=width,height', '-of', 'csv=p=0:s=x', video_file], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    video_size = re.findall('\d+', result.stdout.decode())[0:2]
    video_width, video_height = map(int, video_size)

    # Get video duration
    ffprobe_command = f'ffprobe -i "{video_file}" -show_entries format=duration -v quiet -of csv="p=0"'
    video_duration = subprocess.check_output(ffprobe_command, shell=True)
    video_duration = float(video_duration.decode('utf-8').strip())

    # Set the start time of text
    text_start_time = 1

    # create a folder for this customer if it doesn't exist
    output_path = f"{output_folder}/{customer_name}"
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    # remove chars from versesource for the name
    text_source_for_name = text_source.replace(":", "").rstrip('\n')

    # Create image of verse
    created_verse_image = create_image(text_verse, fonts[random_font_num], fonts_sizes[random_font_num], fonts_maxcharline[random_font_num], (int(video_width), int(video_height / 2)), verse_text_image_path, text_source_for_name)

    # fix bug that ':' and beyond wasn't showing on screen
    text_source = text_source.replace(':', '\:')
    text_source_for_name = text_source_for_name.replace(' ', '')
    output_path += f"/{i}-{text_source_for_name}_{random_video_num}_{random_audio_num}_{random_font_num}.mp4"
    # FFMPEG command to overlay images and text onto input video
    ffmpeg_command = (f'ffmpeg -y -loop 1 -i "{image_path}" -i "{audio_file}" '
                      f'-i "{video_file}" -i "{created_verse_image}" -r 24 -filter_complex '
                      f'"[2:v][0:v]overlay=(W-w)/2:{image_y}[v1]; '
                      # f'[v1]drawtext=fontfile={selected_font}:text=\'{text_verse}\':x=(w-text_w)/2:y=(h-text_h)/2:fontsize=60:fontcolor=white:'
                      # f'enable=\'between(t,{text_start_time},{video_duration})\'[v2]; '
                      f'[v1]drawtext=fontfile=\'{text_source_font}\':text=\'{text_source}\':x=(w-text_w)/2:y={text2_y}:fontsize=42:fontcolor=white:'
                      f'enable=\'between(t,{text_start_time},{video_duration})\'[v2]; '
                      f'[v2][3:v]overlay=(W-w)/2:{video_height}/4:enable=\'between(t,{text_start_time},{video_duration})\'[v3]" '
                      f'-t {video_duration} -map "[v3]" -map 1:a -c:v libx264 -preset veryfast -crf 18 -c:a copy "{output_path}"')

    # # WITHOUT LOGO
    # ffmpeg_command = (f'ffmpeg -y -i "{audio_file}" '
    #                   f'-i "{video_file}" -i "{created_verse_image}" -r 24 -filter_complex '
    #                   # f'[v1]drawtext=fontfile={selected_font}:text=\'{text_verse}\':x=(w-text_w)/2:y=(h-text_h)/2:fontsize=60:fontcolor=white:'
    #                   # f'enable=\'between(t,{text_start_time},{video_duration})\'[v2]; '
    #                   f'"drawtext=fontfile=\'{text_source_font}\':text=\'{text_source}\':x=(w-text_w)/2:y={text2_y}:fontsize=42:fontcolor=white:'
    #                   f'enable=\'between(t,{text_start_time},{video_duration})\'[v1]; '
    #                   f'[v1][2:v]overlay=(W-w)/2:{video_height}/4:enable=\'between(t,{text_start_time},{video_duration})\'[v2]" '
    #                   f'-t {video_duration} -map "[v2]" -map 0:a -c:v libx264 -preset veryfast -crf 18 -c:a copy "{output_path}"')

    # Run FFMPEG command
    subprocess.call(ffmpeg_command, shell=True)

    end_time = time.time()
    run_time = end_time - start_time
    run_time_average += run_time
    print(f"\033[0;34m DONE #{i}, Run time:", round(run_time, 2), "seconds! \033[0m", output_path)

if number_of_videos > 1:
    run_time_average /= number_of_videos
    end_time_total = time.time()
    run_time_total = end_time_total - start_time_total
    print(f"\n\033[0;32mDone making {number_of_videos} videos for {customer_name}!"
          f"\nTotal run time:", round(run_time_total, 2), "seconds!"
          f"\nAverage run time:", round(run_time_average, 2), "seconds! \033[0m")



