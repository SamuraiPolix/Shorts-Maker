import random
import moviepy.video.fx.all as vfx
import moviepy.video.VideoClip as vc
import moviepy.video.compositing.CompositeVideoClip as cvc
import moviepy.video.io.VideoFileClip as vfc
import moviepy.audio.AudioClip as ac
import moviepy.audio.io.AudioFileClip as afc
import sys
import os


def generate_video(video_folder, new_video_folder):
    # Get a list of video files in the specified folder
    video_files = [f"{video_folder}/{file}" for file in os.listdir(video_folder) if file.endswith(".mp4")]

    for current_video in video_files:
        # Load the video file without audio
        video_clip = (vfc.VideoFileClip(current_video, audio=False)
                      .on_color(color=(255, 255, 255), col_opacity=1)
                      .set_opacity(0.8)
                      .without_audio())

        # if fps is higher than 30, drop it to 30 to save space
        if video_clip.fps > 30:
            video_clip.set_fps(30)

        # if video is longer than 20s, drop it to 20 to save space
        if video_clip.duration > 20:
            video_clip.subclip(0, 20)

        # Set the maximum length to 15 minutes (in seconds)
        # max_length = 15
        # if video_clip.duration > max_length:
        #     video = video_clip.subclip(0, max_length)

        # Overlay the text on the video
        final_clip = cvc.CompositeVideoClip([video_clip])

        # Save the final video
        final_clip.write_videofile(f"{current_video}")


def setup():
    video_folder = "E:/Bots/VideoMaker/test"
    if not os.path.exists("new_videos"):
        os.makedirs("new_videos")
    new_video_folder = f"{video_folder}/new_videos"
    generate_video(video_folder, new_video_folder)
