import os
import random
import subprocess
import re

# TODO: set good positions
# Define the paths to the input video, output video, image file, audio file, text path, and number of videos to produce
video_folder = "E:/Bots/VideoMaker/videos/1.mp4"
audio_folder = "E:/Bots/VideoMaker/audio/new audio/ambient-piano-10781.mp3"
text_path = "E:/Bots/VideoMaker/sources/text.txt"
# font_dir = "C:/Windows/Fonts"
image_path = "E:/Bots/VideoMaker/sources/logo.png"
number_of_videos = 10
fonts = ['Want-Coffee']

# Read the text file into a list of lines
with open(text_path, 'r', encoding='utf-8') as file:
    text = file.readlines()

for i in range(number_of_videos):
    print(f"Creating Video #{i}")
    curr_text = text[i]
    text_parts = curr_text.split('|')
    text_verse = text_parts[0]
    text_source = text_parts[1]

    # Get a list of video files in the specified folder
    video_files = [f"{video_folder}/{file}" for file in os.listdir(video_folder) if file.endswith(".mp4")]

    # Choose a random video file from the list
    # random_video_num = random.randint(0, len(video_files) - 1)
    # video_file = video_files[random_video_num]
    video_file = random.choice(video_files)
    random_video_num = video_file.split('/')
    random_video_num = random_video_num[len(random_video_num)-1].split('.')
    random_video_num = random_video_num[0]

    # Choose a random font from list
    random_font_num = random.randint(0, len(fonts) - 1)
    selected_font = fonts[random_font_num]

    # Get a list of audio files in the specified folder
    audio_files = [f"{audio_folder}/{file}" for file in os.listdir(audio_folder) if file.endswith(".wav")]

    # Choose a random video file from the list
    random_audio_num = random.randint(0, len(audio_files) - 1)
    audio_file = audio_files[random_audio_num]

    # Choose a random font from list
    random_font_num = random.randint(0, len(fonts) - 1)
    selected_font = fonts[random_font_num]

# Text strings and fonts
text1 = "VERSE"
text2 = "SOURCE"
fonts = os.listdir(font_dir)
random_font = os.path.join(font_dir, random.choice(fonts))

# Output video file path
output_path = "E:/Bots/VideoMaker/output.mp4"

# Coordinates of image and text clips (default: 0, 0)
# image_x = 0
image_y = 1600
# text1_x = 0
# text1_y = 1920/2
# text2_x = 0
text2_y = 1300

# Get the video size
result = subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'stream=width,height', '-of', 'csv=p=0:s=x', video_path], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
video_size = re.findall('\d+', result.stdout.decode())[0:2]
video_width, video_height = map(int, video_size)

# Set the start time of text
text_start_time = 1

# Calculate the font size
fontsize = min(video_width // len(text1), video_height // 2)
# Calculate the maximum width of each line
text_max_width = int(0.8 * video_width)

# Replace any instances of '\n' with a space
text1 = text1.replace('\n', ' ')
text2 = text2.replace('\n', ' ')


ffprobe_command = f'ffprobe -i "{video_path}" -show_entries format=duration -v quiet -of csv="p=0"'
video_duration = subprocess.check_output(ffprobe_command, shell=True)
video_duration = float(video_duration.decode('utf-8').strip())
print(video_duration)
# FFMPEG command to overlay image and text onto input video
ffmpeg_command = (f'ffmpeg -y -loop 1 -i "{image_path}" -i "{audio_file}" '
                  f'-i "{video_file}" -r 24 -filter_complex '
                  f'"[2:v][0:v]overlay=(W-w)/2:{image_y}[v1]; '
                  f'[v1]drawtext=fontfile={selected_font}:text={text_verse}:x=(w-text_w)/2:y=(h-text_h)/2:fontsize={fontsize}:fontcolor=white:'
                  f'wrap={text_max_width}:lh=1.5:'
                  # f'box=1:boxborderw=1000:boxcolor=0xffffff:'
                  f'enable=\'between(t,{text_start_time},{video_duration})\'[v2]; '
                  f'[v2]drawtext=fontfile={selected_font}:text={text_source}:x=(w-text_w)/2:y={text2_y}:fontsize=36:fontcolor=white:'
                  f'enable=\'between(t,{text_start_time},{video_duration})\'[v3]" '
                  f'-t {video_duration} -map "[v3]" -map 1:a -c:v libx264 -preset veryfast -crf 18 -c:a copy "{output_path}"')


# Run FFMPEG command
subprocess.call(ffmpeg_command, shell=True)

print("DONE!")
