import os
import ffmpeg
import json_handler
import verse_handler
from Fonts import Fonts

# Define paths and values
number_of_videos = 1
project_dir = os.getcwd().replace("\\", "/")

video_folder = f"{project_dir}/videos"
audio_folder = f"{project_dir}/audio"
json_file = f"{project_dir}/sources/verses_data/love_data.json"
fonts_dir = f"{project_dir}/sources/fonts"
output_folder = f"{project_dir}/customers"
text_source_font = f'{project_dir}/sources/MouldyCheeseRegular-WyMWG.ttf'.replace(":/", "\:/")
image_file = f"{project_dir}/sources/logo.png"
customer_name = "your_name"
verse_text_image_path = f"{project_dir}/verse_images/{customer_name}"
fonts_paths = [f'{project_dir}/sources/fonts/CoffeeJellyUmai.ttf', f'{project_dir}/sources/fonts/CourierprimecodeRegular.ttf', f'{project_dir}/sources/fonts/FlowersSunday.otf', f'{project_dir}/sources/fonts/GreenTeaJelly.ttf', f'{project_dir}/sources/fonts/HeyMarch.ttf', f'{project_dir}/sources/fonts/LetsCoffee.otf', f'{project_dir}/sources/fonts/LikeSlim.ttf', f'{project_dir}/sources/fonts/SunnySpellsBasicRegular.ttf', f'{project_dir}/sources/fonts/TakeCoffee.ttf', f'{project_dir}/sources/fonts/WantCoffee.ttf']
fonts_sizes = [95, 70, 65, 85, 75, 50, 75, 87, 50, 65]
fonts_maxcharsline = [34, 25, 30, 45, 33, 34, 35, 32, 35, 35]
# project_dir = os.getcwd()
# font_dir = "C:/Windows/Fonts"


if __name__ == "__main__":
    fonts = Fonts(fonts_paths, fonts_sizes, fonts_maxcharsline)

    # Create a file for estimated runtime calculation if it doesn't exist yet
    open(f"{project_dir}/runtime.pk", 'a').close()

    ffmpeg.create_videos(video_folder=video_folder, audio_folder=audio_folder, fonts=fonts, json_file=json_file,
                         fonts_dir=fonts_dir, output_folder=output_folder, text_source_font=text_source_font,
                         image_file=image_file, customer_name=customer_name, number_of_videos=number_of_videos)

