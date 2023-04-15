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


video_folder = "E:/Bots/VideoMaker/videos/original/new ones"
output_folder = "E:/Bots/VideoMaker/videos"
DARK = 0.8
generate_darken_videos(video_folder, output_folder)
# Specific video
# video_file = "E:/Bots/VideoMaker/videos/original/7.mp4"
# output_path = "E:/Bots/VideoMaker/videos/darken 40%/7.mp4"
# generate_darken_video(video_file, output_path)



