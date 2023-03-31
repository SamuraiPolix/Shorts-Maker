import os
import random
import subprocess


def generate_video(video_folder, audio_folder, text_file, fonts, logo_file, channel_name, number):
    # Read the text file into a list of lines
    with open(text_file, 'r', encoding='utf-8') as file:
        text = file.readlines()

    for i in range(number):
        print(f"Creating Video #{i}")
        curr_text = text[i]
        text_parts = curr_text.split('|')
        text_source = text_parts[1]
        text_verse = text_parts[0]

        # Get a list of video files in the specified folder
        video_files = [f"{video_folder}/{file}" for file in os.listdir(video_folder) if file.endswith(".mp4")]

        # Choose a random video file from the list
        video_file = random.choice(video_files)
        random_video_num = video_file.split('/')
        random_video_num = random_video_num[len(random_video_num) - 1].split('.')
        random_video_num = random_video_num[0]

        # Choose a random font from list
        random_font_num = random.randint(0, len(fonts) - 1)
        selected_font = fonts[random_font_num]

        # Get a list of audio files in the specified folder
        audio_files = [f"{audio_folder}/{file}" for file in os.listdir(audio_folder) if file.endswith(".wav")]

        # Choose a random video file from the list
        random_audio_num = random.randint(0, len(audio_files) - 1)
        audio_file = audio_files[random_audio_num]

        # Load the video file without audio
        video_clip = (
            f"ffmpeg -i {video_file} -an -filter:v \"color=white@0.8:1920x1080 [bg];[bg][0:v]overlay=shortest=1\" -y temp_video.mp4")
        subprocess.call(video_clip, shell=True)

        # if fps is higher than 30, drop it to 30 to save space
        video_fps = float(subprocess.check_output(
            f"ffprobe -v error -select_streams v:0 -show_entries stream=r_frame_rate -of default=noprint_wrappers=1:nokey=1 {video_file}").strip().decode())
        if video_fps > 30:
            fps_clip = f"ffmpeg -i temp_video.mp4 -filter:v \"minterpolate='mi_mode=mci:me=hexbs:mc_mode=aobmc:me_mode=bidir:vsbmc=1:fps={30}'\" -y temp_video_fps.mp4"
            subprocess.call(fps_clip, shell=True)
            video_file = "temp_video_fps.mp4"

        # if video is longer than 20s, drop it to 20 to save space
        video_duration = float(subprocess.check_output(
            f"ffprobe -v error -select_streams v:0 -show_entries format=duration -of default=noprint_wrappers=1:nokey=1 {video_file}").strip().decode())
        if video_duration > 20:
            duration_clip = f"ffmpeg -i {video_file} -t 20 -c copy -y temp_video_duration.mp4"
            subprocess.call(duration_clip, shell=True)
            video_file = "temp_video_duration.mp4"

        # Fade in and fade out audio
        audio_clip = f"ffmpeg -i {audio_file} -af afade=t=in:st=0:d=1.5,afade=t=out:st={video_duration - 1.5}:d=
