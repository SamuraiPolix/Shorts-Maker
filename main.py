import ffmpeg
import verse_handler
from Fonts import Fonts

# Define the paths and values to everything
number_of_videos = 1
video_folder = "E:/Bots/VideoMaker/videos"
# video_folder = "E:/Bots/VideoMaker/videos/caribbean/darken0.4"
audio_folder = "E:/Bots/VideoMaker/audio"
json_file = "E:/Bots/VideoMaker/sources/verses_data/love_data_KJV.json"
fonts_dir = "E:/Bots/VideoMaker/sources/fonts"
output_folder = "E:/Bots/VideoMaker/customers"
text_source_font = r"E\:/Bots/VideoMaker/sources/MouldyCheeseRegular-WyMWG.ttf"
image_file = "E:/Bots/VideoMaker/sources/logoNotSqueezed.png"
customer_name = "nigelwilliam646_not_squeezed1"
verse_text_image_path = f"E:/Bots/VideoMaker/verse_images/{customer_name}"
fonts_paths = ['E:/Bots/VideoMaker/sources/fonts/CoffeeJellyUmai.ttf', 'E:/Bots/VideoMaker/sources/fonts/CourierprimecodeRegular.ttf', 'E:/Bots/VideoMaker/sources/fonts/EbGaramond08Regular-2mWe.ttf', 'E:/Bots/VideoMaker/sources/fonts/FlowersSunday.otf', 'E:/Bots/VideoMaker/sources/fonts/GreenTeaJelly.ttf', 'E:/Bots/VideoMaker/sources/fonts/HeyMarch.ttf', 'E:/Bots/VideoMaker/sources/fonts/Hugamour.ttf', 'E:/Bots/VideoMaker/sources/fonts/LetsCoffee.otf', 'E:/Bots/VideoMaker/sources/fonts/Lightning Script.ttf', 'E:/Bots/VideoMaker/sources/fonts/LikeSlim.ttf', 'E:/Bots/VideoMaker/sources/fonts/PineappleDays.ttf', 'E:/Bots/VideoMaker/sources/fonts/SunnySpellsBasicRegular.ttf', 'E:/Bots/VideoMaker/sources/fonts/TakeCoffee.ttf', 'E:/Bots/VideoMaker/sources/fonts/WantCoffee.ttf']
fonts_sizes = [95, 70, 70, 65, 85, 75, 73, 50, 85, 75, 52, 87, 50, 65]
fonts_maxcharsline = [34, 25, 35, 30, 45, 35, 32, 34, 35, 35, 35, 32, 35, 35]
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
    ffmpeg.create_videos(video_folder=video_folder, audio_folder=audio_folder, fonts=fonts, json_file=json_file,
                         fonts_dir=fonts_dir, output_folder=output_folder, text_source_font=text_source_font,
                         image_file=image_file, customer_name=customer_name, number_of_videos=number_of_videos)

    # verse_handler.create_sheets(f'E:/Bots/VideoMaker/customers/{customer_name}', json_file)