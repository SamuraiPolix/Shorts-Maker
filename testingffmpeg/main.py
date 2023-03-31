import subprocess

# Define the paths to the input video, output video, image file, audio file, and number of videos to produce
input_video_path = "input_video.mp4"
output_video_path = "output_video.mp4"
image_path = "image.jpg"
audio_path = "audio.mp3"
number_of_videos = 10

# Define the FFMPEG command to overlay the image onto the video and replace the audio
ffmpeg_cmd = [
    "ffmpeg",
    "-i", input_video_path,  # Input video file
    "-i", image_path,  # Input image file
    "-i", audio_path,  # Input audio file
    "-filter_complex",
    "[0:v][1:v]overlay=(main_w-overlay_w)/2:(main_h-overlay_h)/2:shortest=1[v]",  # Overlay the image onto the video
    "-map", "[v]",  # Map the output video stream from the overlay filter
    "-map", "2:a",  # Map the input audio stream
    "-c:v", "libx264",  # Video codec
    "-preset", "fast",  # Encoding preset
    "-crf", "18",  # Constant rate factor
    "-c:a", "copy",  # Copy the audio track without re-encoding
    "-pix_fmt", "yuv420p",  # Pixel format
    "-y",  # Overwrite the output file if it already exists
    output_video_path  # Output file path
]

# Run the FFMPEG command
subprocess.run(ffmpeg_cmd)

import subprocess

# Define the FFMPEG command
ffmpeg_cmd = ['ffmpeg', '-i', '1.mp4', '-vf', "drawtext=text='Hello World':fontfile=/path/to/font.ttf:fontsize=50:x=100:y=100:fontcolor=white", '-codec:a', 'copy', 'output_video.mp4']

# Execute the FFMPEG command
subprocess.call(ffmpeg_cmd)

