import os
import pickle
import random
import subprocess
import re
import sys
import time
import json_handler
import verse_handler
import Fonts
import cv2


def create_dirs(output_folder, customer_name, posts=True):
    # create a folder for this customer if it doesn't exist
    output_path = f"{output_folder}/{customer_name}"
    if not os.path.exists(output_path):
        os.makedirs(output_path)
    # Create folder inside for images
    if not os.path.exists(f"{output_path}/verse_images"):
        os.makedirs(f"{output_path}/verse_images")
    if posts and not os.path.exists(f"{output_path}/post_images"):
        os.makedirs(f"{output_path}/post_images")
    return output_path


def create_videos(video_folder, audio_folder, json_file, fonts_dir, output_folder, text_source_font, image_file: str,
                  customer_name, number_of_videos, fonts: Fonts, posts=False):
    json_data = json_handler.get_data(json_file)
    verses: str = json_data[0]
    refs: str = json_data[1]

    if number_of_videos == -1:
        number_of_videos = len(verses) - 1
    run_time_average = 0
    if number_of_videos > 1:
        start_time_total = time.time()

    videos_num = list()
    audios_num = list()
    fonts_num = list()

    # Get lists of video and audio files in the specified folders
    video_files = [f"{video_folder}/{file}" for file in os.listdir(video_folder) if file.endswith(".mp4")]
    audio_files = [f"{audio_folder}/{file}" for file in os.listdir(audio_folder) if file.endswith(".mp3")]
    random_for_video = random.randint(0, len(video_files) - 1)
    random_for_audio = random.randint(0, len(audio_files) - 1)
    random_for_font = random.randint(0, len(fonts.fonts_path) - 1)
    for i in range(number_of_videos):
        videos_num.append((random_for_video + i) % len(video_files))
        audios_num.append((random_for_audio + i) % len(audio_files))
        fonts_num.append((random_for_font + i) % len(fonts.fonts_path))
    random.shuffle(videos_num)
    random.shuffle(audios_num)
    random.shuffle(fonts_num)

    # Creating folder for customer
    output_path = create_dirs(output_folder, customer_name, posts)

    # Data for spreadsheet
    spreadsheet_col1 = list()
    spreadsheet_col2 = list()
    spreadsheet_col3 = list()

    avg_runtime = get_avg_runtime('runtime.pk')
    if avg_runtime != -1:
        estimated_runtime = round(avg_runtime * number_of_videos, 2)
        # seconds
        print(f"\033[0;32mEstimated run time: ", round(estimated_runtime, 2), " seconds\033[0m")
        if round(estimated_runtime, 2) > 60:  # minutes
            print("\033[0;32m = ", round(estimated_runtime / 60, 2), " minutes\033[0m")
        if round(estimated_runtime / 60, 2) > 60:  # hours
            print("\033[0;32m = ", round((estimated_runtime / 60) / 60, 2), " hours\033[0m")
        print("\033[0;32mfor ", number_of_videos, " videos!\033[0m")

    for i in range(number_of_videos):
        start_time = time.time()
        print(f"Creating Video #{i}")

        text_verse = verses[i]
        text_source = refs[i]

        # Choose a random video file from the list
        random_video_num = videos_num[0]
        del videos_num[0]
        video_file = video_files[random_video_num]
        # video_file = f"{video_folder}/30.mp4"

        # Choose a random font from list
        random_font_num = fonts_num[0]
        del fonts_num[0]
        font_file = fonts.fonts_path[random_font_num]
        font_size = fonts.fonts_size[random_font_num]
        font_chars = fonts.fonts_chars_limit[random_font_num]

        # Choose a random audio file from the list
        random_audio_num = audios_num[0]
        del audios_num[0]
        audio_file = audio_files[random_audio_num]

        # remove chars from versesource for the name
        text_source_for_image = text_source.replace(":", "").rstrip('\n')
        text_source_for_name = text_source_for_image.replace(' ', '')

        file_name = f"/{i}-{text_source_for_name}_{random_video_num}_{random_audio_num}_{random_font_num}.mp4"

        create_video(text_verse=text_verse, text_source=text_source, text_source_font=text_source_font,
                     text_source_for_image=text_source_for_image,
                     video_file=video_file, audio_file=audio_file, image_file=image_file,
                     font_file=font_file, font_size=font_size, font_chars=font_chars,
                     posts=posts,
                     output_path=output_path, file_name=file_name)

        spreadsheet_col1.append(file_name.strip("/"))
        spreadsheet_col2.append(text_source)
        spreadsheet_col3.append(text_verse)

        end_time = time.time()
        run_time = end_time - start_time
        run_time_average += run_time
        print(f"\033[0;34m DONE #{i}, Run time:", round(run_time, 2), "seconds! \033[0m", output_path)

    # add file to spreadsheet
    verse_handler.add_sheets(video_names=spreadsheet_col1, customer_name=customer_name, output_path=output_path,
                             refs=spreadsheet_col2, verses=spreadsheet_col3)

    if number_of_videos > 1:
        run_time_average /= number_of_videos
        update_avg_runtime(filename='runtime.pk', curr_runtime=run_time_average)
        end_time_total = time.time()
        run_time_total = end_time_total - start_time_total
        print(f"\n\033[0;32mDone making {number_of_videos} videos for {customer_name}!"
              f"\nTotal run time:", round(run_time_total, 2), "seconds = ", round(run_time_total / 60, 2), " minutes!",
              f"\nAverage run time:", round(run_time_average, 2), "seconds! \033[0m")


def create_video(text_verse, text_source, text_source_font, text_source_for_image, video_file: str, audio_file,
                 image_file,
                 font_file, font_size, font_chars, output_path, file_name, posts=True):
    # Coordinates of logo image and text2 clips
    image_y = 0
    image_text_source_y = 800

    # Get the video size
    result = subprocess.run(
        ['ffprobe', '-v', 'error', '-show_entries', 'stream=width,height', '-of', 'csv=p=0:s=x', video_file],
        stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    video_size = re.findall('\d+', result.stdout.decode())[0:2]
    video_width, video_height = map(int, video_size)

    # Get video duration
    ffprobe_command = f'ffprobe -i "{video_file}" -show_entries format=duration -v quiet -of csv="p=0"'
    video_duration = subprocess.check_output(ffprobe_command, shell=True)
    video_duration = float(video_duration.decode('utf-8').strip())

    # Set the start time of text
    text_start_time = 1

    text_color = (255, 255, 255, 255)
    font_color = "white"

    # Create image of verse
    created_verse_image_data = verse_handler.create_image(text_verse, font_file, font_size, font_chars,
                                                          (int(video_width), int(video_height / 2)), output_path,
                                                          text_source_for_image, text_color=text_color)
    created_verse_image = created_verse_image_data[0]
    verse_height = created_verse_image_data[1]

    text2_y: int = image_text_source_y + verse_height + 75

    # If ref text leaps to logo, move it to 1200, and adjust the verse accordingly
    if (text2_y > 1200):
        diff = text2_y - 1200
        text2_y = 1200
        image_text_source_y -= diff

    # print(f"{image_text_source_y}, {text2_y}")

    # fix bug that ':' and beyond wasn't showing on screen
    text_source = text_source.replace(':', '\:')
    output_folder = output_path
    output_path += f"/{file_name}"
    # FFMPEG command to overlay images and text onto input video
    ffmpeg_command = (f'ffmpeg -loglevel error -stats -y -loop 1 -i "{image_file}" -i "{audio_file}" '
                      f'-i "{video_file}" -i "{created_verse_image}" -r 24 -filter_complex '
                      f'"[2:v][0:v]overlay=(W-w)/2:{image_y}[v1]; '
                      # f'[v1]drawtext=fontfile={selected_font}:text=\'{text_verse}\':x=(w-text_w)/2:y=(h-text_h)/2:fontsize=60:fontcolor=white:'
                      # f'enable=\'between(t,{text_start_time},{video_duration})\'[v2]; '
                      f'[v1]drawtext=fontfile=\'{text_source_font}\':text=\'{text_source}\':x=(w-text_w)/2:y={text2_y}:fontsize=42:fontcolor={font_color}:'
                      f'enable=\'between(t,{text_start_time},{video_duration})\'[v2]; '
                      f'[v2][3:v]overlay=(W-w)/2:{image_text_source_y}:enable=\'between(t,{text_start_time},{video_duration})\'[v3]" '
                      f'-t {video_duration} -map "[v3]" -map 1 -c:v libx264 -preset veryfast -crf 18 "{output_path}"')
    # WITHOUT LOGO
    # ffmpeg_command = (f'ffmpeg -loglevel error -stats -y -loop 1 -i "{audio_file}" '
    #                   f'-i "{video_file}" -i "{created_verse_image}" -r 24 -filter_complex '
    #                   # f'[v1]drawtext=fontfile={selected_font}:text=\'{text_verse}\':x=(w-text_w)/2:y=(h-text_h)/2:fontsize=60:fontcolor=white:'
    #                   # f'enable=\'between(t,{text_start_time},{video_duration})\'[v2]; '
    #                   f'"[v1]drawtext=fontfile=\'{text_source_font}\':text=\'{text_source}\':x=(w-text_w)/2:y={text2_y}:fontsize=42:fontcolor={font_color}:'
    #                   f'enable=\'between(t,{text_start_time},{video_duration})\'[v2]; '
    #                   f'[v2][2:v]overlay=(W-w)/2:{image_text_source_y}:enable=\'between(t,{text_start_time},{video_duration})\'[v3]" '
    #                   f'-t {video_duration} -map "[v3]" -map 1 -c:v libx264 -preset veryfast -crf 18 "{output_path}"')

    # Run FFMPEG command
    try:
        subprocess.check_call(ffmpeg_command)
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")
        sys.exit()

    if posts:
        verse_handler.create_post_images(video_path=output_path, output_folder=f"{output_folder}/post_images")


def create_post_images(video_path: str, verse_image_path, text_source, output_folder):
    # Open the video file
    video = cv2.VideoCapture(video_path)

    # Get the frame rate of the video
    fps = int(video.get(cv2.CAP_PROP_FPS))

    # Set the time in seconds to extract a frame from
    time_in_seconds = 2

    # Calculate the frame index to extract
    frame_index = time_in_seconds * fps

    # Set the output image size
    output_size = (1080, 1080)

    # Loop through the video frames until we reach the desired frame
    for i in range(frame_index):
        ret, frame = video.read()

    # Crop the middle square of the frame
    height, width, channels = frame.shape
    y = 325
    cropped_frame = frame[y:y + 1440, 0:width]

    # Resize the cropped frame to the output size
    # resized_frame = cv2.resize(cropped_frame, output_size)

    # Save the frame as an image
    output_name = video_path.split('/')
    output_name = output_name[len(output_name) - 1].strip(".mp4")
    cv2.imwrite(f"{output_folder}/post_images/{output_name}.jpg", cropped_frame)

    # Release the video file
    video.release()


def get_avg_runtime(filename: str):
    with open(filename, 'rb') as fi:
        try:
            return pickle.load(fi)
        except EOFError:    # If file is empty because it's the first run
            return -1



def update_avg_runtime(curr_runtime: float, filename: str):
    old_runtime = get_avg_runtime(filename)

    new_runtime = (old_runtime + curr_runtime) / 2

    with open(filename, 'wb') as fi:
        # dump your data into the file
        pickle.dump(new_runtime, fi)
