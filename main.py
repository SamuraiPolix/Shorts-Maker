import random
from trash import createVideosByNumber
import moviepy.audio.fx.all as afx
import moviepy.video.VideoClip as vc
import moviepy.video.compositing.CompositeVideoClip as cvc
import moviepy.video.io.VideoFileClip as vfc
import moviepy.audio.io.AudioFileClip as afc
import os


def generate_video(video_folder, audio_folder, text_file, fonts, logo_file, channel_name):
    # Read the text file into a list of lines
    with open(text_file, 'r', encoding='utf-8') as file:
        text = file.readlines()

    # Choose a random text from the list of lines
    random_text_num = random.randint(0, len(text) - 1)
    text = text[random_text_num]
    text_parts = text.split('|')
    text_source = text_parts[1]
    text = text_parts[0]
    # text = random.choice(text)

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

    # Load the video file without audio
    video_clip = (vfc.VideoFileClip(video_file, audio=False)
                  .on_color(color=(255, 255, 255), col_opacity=1)
                  .set_opacity(0.8)
                  .without_audio())

    # if fps is higher than 30, drop it to 30 to save space
    if video_clip.fps > 30:
        video_clip.set_fps(30)

    # if video is longer than 20s, drop it to 20 to save space
    if video_clip.duration > 20:
        video_clip.subclip(0, 20)

    # # if video is shorter than 10s, slow it down to reach 10s
    # if video_clip.duration < 10:
    #     video_clip.speedx(factor=1/((10/video_clip.duration)-1))

    audio_file_clip = (afc.AudioFileClip(audio_file)
                       .set_duration(video_clip.duration))

    # Define the duration of the fade in and fade out in seconds
    fade_duration = 1.5

    # Fade in the audio clip
    audio_file_clip = afx.audio_fadein(audio_file_clip, fade_duration)

    # Fade out the audio clip
    audio_file_clip = afx.audio_fadeout(audio_file_clip, fade_duration)

    # Set the maximum length to 15 minutes (in seconds)
    # max_length = 15
    # if video_clip.duration > max_length:
    #     video = video_clip.subclip(0, max_length)

    audio_clip = cvc.CompositeAudioClip([audio_file_clip])

    # Bible verse text clip
    # TODO: set good positions
    print(vc.TextClip.list('font'))
    verse_text_clip = (vc.TextClip(text, color='white', font=selected_font, size=(900, 450), method="caption",
                                   align="center")
                       .set_position(("center", "center"))
                       .set_start(1)
                       .set_duration(video_clip.duration - 1))

    # Source of text text clip
    # TODO: set good positions
    source_text_clip = (vc.TextClip(text_source, fontsize=36, color='white', font="Centaur", align="center")
                        .set_position(("center", 1300))
                        .set_start(1)
                        .set_duration(video_clip.duration - 1))

    # Channel name text clip
    # TODO: set good positions
    # name_text_clip = (vc.TextClip(channel_name, fontsize=55, color='white', font="Centaur")
    #                   .set_position((450 + 65, 1650))
    #                   .set_duration(video_clip.duration))

    # TODO: set good positions
    logo_image_clip = (vc.ImageClip(logo_file)
                       .set_position(("center", 1600))
                       .set_duration(video_clip.duration))

    # Overlay the text on the video
    final_clip = cvc.CompositeVideoClip(
        [video_clip, verse_text_clip, source_text_clip, logo_image_clip])
    final_clip.audio = audio_clip

    # create a folder for this customer if doesnt exist
    path = f"E:/Bots/VideoMaker/customers/{channel_name}"
    if not os.path.exists(path):
        os.makedirs(path)

    # Save the final video to E:/Bots/VideoMaker/customers/{channel_name} in format: text-video-audio-font.mp4
    final_clip.write_videofile(f"E:/Bots/VideoMaker/customers/{channel_name}/{random_text_num}-{random_video_num}-{random_audio_num}-{random_font_num}.mp4")

    # Clean up the temporary files
    final_clip.close()


if __name__ == "__main__":
    # setupVideos.setup()
    video_folder = "E:/Bots/VideoMaker/videos"
    audio_folder = "E:/Bots/VideoMaker/audio/shaz/wav"
    text_file = "/trash/text.txt"
    # TODO: edit list of fonts
    fonts = ['Want-Coffee']
    channel_name = "FulminatiX"
    logo_file = "E:/Bots/VideoMaker/sources/logo.png"
    num_of_videos = 5
    # generate_video(video_folder, audio_folder, text_file, fonts, logo_file, channel_name)
    createVideosByNumber.generate_video(video_folder, audio_folder, text_file, fonts, logo_file, channel_name, num_of_videos)

