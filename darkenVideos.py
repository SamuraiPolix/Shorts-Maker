import re
import subprocess
import sys

import moviepy.video.io.VideoFileClip as vfc
import os
from moviepy import video


def generate_darken_video(video_file, output_path):
    video_clip = (vfc.VideoFileClip(video_file, audio=False)
                  .without_audio())

    # Save the final video
    darken_clip = video_clip.fl_image(darken)
    darken_clip.write_videofile(output_path,
                                threads=8,
                                codec="libx264")
    # Clean up the temporary files
    darken_clip.close()


# A defined function to darken the frames
def darken(frame):
    return frame * DARK


def generate_darken_videos(video_folder, output_folder):
    # Get a list of video files in the specified folder
    video_files = [f"{video_folder}/{file}" for file in os.listdir(video_folder) if file.endswith(".mp4")]
    for video_file in video_files:
        video_num = video_file.split('/')
        video_num = video_num[len(video_num) - 1].split('.')
        video_num = video_num[0]

        generate_darken_video(video_file, f"{output_folder}/{video_num}.mp4")


def cut_vertical_to_horizontal(video_folder, output_folder):
    video_files = [f"{video_folder}/{file}" for file in os.listdir(video_folder) if file.endswith(".mp4")]
    i = 0
    for video_file in video_files:
        result = subprocess.run(
            ['ffprobe', '-v', 'error', '-show_entries', 'stream=width,height', '-of', 'csv=p=0:s=x', video_file],
            stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        video_size = re.findall('\d+', result.stdout.decode())[0:2]
        video_width, video_height = map(int, video_size)
        x = (video_width-1080)/2
        y = 0

        # Calculate crop dimensions based on video orientation
        crop_height = 1080
        crop_width = crop_height / (16/9)

        out = f"{output_folder}/vid{i}.mp4"
        # Run ffmpeg to crop the video
        cmd = [
            'ffmpeg', '-i', video_file,
            '-vf', f'crop={crop_width}:{crop_height}:(in_w-{crop_width})/2:(in_h-{crop_height})/2,scale=1080:1920',
            '-c:a', 'copy', out
        ]

        try:
            subprocess.check_call(cmd, shell=True)
        except subprocess.CalledProcessError as e:
            # Handle the exception here
            print(f"An error occurred: {e}")
            sys.exit()

        i += 1


# video_folder = "E:/Bots/VideoMaker/videos/black_people/cropped"
# output_folder = "E:/Bots/VideoMaker/videos/black_people/cropped/darken"
DARK = 0.8
# generate_darken_videos(video_folder, output_folder)
# cut_vertical_to_horizontal(video_folder, output_folder)


# Specific video
video_file = "E:/Bots/VideoMaker/videos/black_people/cropped/10.mp4"
output_path = "E:/Bots/VideoMaker/videos/black_people/cropped/darken/10.mp4"
generate_darken_video(video_file, output_path)



