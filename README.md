![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
<a href = "https://www.paypal.com/donate/?hosted_button_id=5JK8CUWFUU9B6">![PayPal](https://img.shields.io/badge/PayPal-00457C?style=for-the-badge&logo=paypal&logoColor=white)</a>

# Quote Video Maker for Shorts/Reels/TikTok
<h3>This script creates high-quality vertical quotes videos (1920x1080) in about 15secs per video!</h3>

https://github.com/SamuraiPolix/ShortsMaker/assets/52662032/bf84a603-f397-4d3c-9d2a-4b2a95da0a8f

This is my first big Python project, which I put a lot of effort into, hope you get the most out of it :)

I used it to sell bible verse videos on Fiverr for a while.

The script works by taking a background video from '/videos', an audio file from '/audios', a random font, and a quote (a bible verse) from the JSON file, and combining them all into 1 video.

<h2>How it works:</h2>

I am using **PILLOW** to generate the text in different fonts and **FFMPEG** to combine them all as fast as possible (I used **MoviePy** at the beginning but it was too slow).

All the video files and audio files are copyright-free from stock footage websites (Pexels, Pixabay, etc.), and the fonts are copyright-free as well.

<h2>How to run:</h2>
<h3>Using an IDE:</h3>

- Open main.py

- set the number of videos you want, your logo, and choose a quote file from '/sources/verses_data' (you can also use the <a href="https://github.com/SamuraiPolix/openbible-verse-scraper">topical bible verses scraper</a> I developed)

```python
number_of_videos = 99
customer_name = "your_name"
image_file = f"{project_dir}/sources/logo.png"
json_file = f"{project_dir}/sources/verses_data/love_data.json"
```
- RUN!

<h2>Results:</h2>

https://github.com/SamuraiPolix/ShortsMaker/assets/52662032/2a4ba17b-ddcd-47d3-82cd-78d0173a3dec

We also generate a **Spreadsheet (.csv file)** with all the File names, verses, and references, to make it easier to find the video you want:
![image](https://github.com/SamuraiPolix/ShortsMaker/assets/52662032/9ffb768a-ea14-4e35-b1cd-e3a27ad2dddf)

And you have access to the generated text images:

<img src="https://github.com/SamuraiPolix/ShortsMaker/assets/52662032/a0226a8f-47a2-4054-83f0-6a7258ed5e34" width="45%">


