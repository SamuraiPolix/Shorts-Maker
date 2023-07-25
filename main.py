import os
import ffmpeg
import json_handler
import verse_handler
from Fonts import Fonts

# Define the paths and values to everything
number_of_videos = 7
project_dir = os.getcwd().replace("\\", "/")

video_folder = f"{project_dir}/videos/poeticpoetry/black_people/women/walking"
# video_folder = "E:/Bots/VideoMaker/videos/caribbean/darken0.4"
audio_folder = f"{project_dir}/audio"
json_file = f"{project_dir}/sources/verses_data/poeticpoetry_data_NEW_pray2.json"
fonts_dir = f"{project_dir}/sources/fonts"
output_folder = f"{project_dir}/customers"
text_source_font = f'{project_dir}/sources/MouldyCheeseRegular-WyMWG.ttf'.replace(":/", "\:/")
image_file = f"{project_dir}/sources/poeticpoetry2.png"
customer_name = "poeticpoetry_black_walking"
verse_text_image_path = f"{project_dir}/verse_images/{customer_name}"
fonts_paths = [f'{project_dir}/sources/fonts/CoffeeJellyUmai.ttf', f'{project_dir}/sources/fonts/CourierprimecodeRegular.ttf', f'{project_dir}/sources/fonts/FlowersSunday.otf', f'{project_dir}/sources/fonts/GreenTeaJelly.ttf', f'{project_dir}/sources/fonts/HeyMarch.ttf', f'{project_dir}/sources/fonts/LetsCoffee.otf', f'{project_dir}/sources/fonts/LikeSlim.ttf', f'{project_dir}/sources/fonts/SunnySpellsBasicRegular.ttf', f'{project_dir}/sources/fonts/TakeCoffee.ttf', f'{project_dir}/sources/fonts/WantCoffee.ttf']
fonts_sizes = [95, 70, 65, 85, 75, 50, 75, 87, 50, 65]
fonts_maxcharsline = [34, 25, 30, 45, 33, 34, 35, 32, 35, 35]
# project_dir = os.getcwd()
# font_dir = "C:/Windows/Fonts"


if __name__ == "__main__":
    fonts = Fonts(fonts_paths, fonts_sizes, fonts_maxcharsline)
    '''
    customer_names = list()
    json_file = list()
    customer_names = [f'{customer_name}_faith', f'{customer_name}_motivation', f'{customer_name}_patience', f'{customer_name}_peace', f'{customer_name}_spiritual_growth', f'{customer_name}_kindness', f'{customer_name}_joy', f'{customer_name}_goodness']
    json_files = ["E:/Bots/VideoMaker/sources/verses_data/faith_data.json", "E:/Bots/VideoMaker/sources/verses_data/motivation_data.json","E:/Bots/VideoMaker/sources/verses_data/patience_data.json", "E:/Bots/VideoMaker/sources/verses_data/peace_data.json", "E:/Bots/VideoMaker/sources/verses_data/spiritual_growth_data.json", "E:/Bots/VideoMaker/sources/verses_data/kindness_data.json", "E:/Bots/VideoMaker/sources/verses_data/joy_data.json", "E:/Bots/VideoMaker/sources/verses_data/goodness_data.json"]
    for i in range(len(customer_name)):
        ffmpeg.create_videos(video_folder=video_folder, audio_folder=audio_folder, fonts=fonts, json_file=json_files[i],
                             fonts_dir=fonts_dir, output_folder=output_folder, text_source_font=text_source_font,
                             image_file=image_file, customer_name=customer_names[i], number_of_videos=number_of_videos)
'''
    # new_json_file = f"{project_dir}/sources/verses_data/poeticpoetry_data_NEW_pray.json"
    # new_new_json_file = f"{project_dir}/sources/verses_data/poeticpoetry_data_NEW_pray2.json"
    # json_handler.fix_json_structure(json_file, new_json_file)
    # json_handler.restore_json_structure(new_json_file, new_new_json_file)
    customer_folder = f"E:/Bots/VideoMaker/customers/cafmax/cafmax_rev/cafmax_rev_rename"
    csv_file = f"{customer_folder}/cafmax_rev.csv"

    verse_handler.rename_videos(customer_folder, csv_file)
    # ffmpeg.create_videos(video_folder=video_folder, audio_folder=audio_folder, fonts=fonts, json_file=json_file,
    #                      fonts_dir=fonts_dir, output_folder=output_folder, text_source_font=text_source_font,
    #                      image_file=image_file, customer_name=customer_name, number_of_videos=number_of_videos)


    # verse_handler.create_sheets(f'E:/Bots/VideoMaker/customers/{customer_name}', json_file)