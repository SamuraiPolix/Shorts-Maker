![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
<a href = "https://www.paypal.com/donate/?hosted_button_id=5JK8CUWFUU9B6">![PayPal](https://img.shields.io/badge/PayPal-00457C?style=for-the-badge&logo=paypal&logoColor=white)</a>

# Quote Video Maker for Shorts/Reels/TikTok
<h3>This script creates high-quality vertical quotes videos (1920x1080) in about 15secs per video!</h3>

## 📝 Table of Contents

1. [About](#about)
2. [Demo](#demo)
3. [How it works](#working)
4. [How To Run](#how_to)
5. [Built Using](#built_using)
6. [Final Results](#results)
7. [Note](#note)

<h2 id="demo">🎥 Demo</h2>

https://github.com/SamuraiPolix/ShortsMaker/assets/52662032/fb67c274-8701-482a-a557-466ce4b9a9ef


<h2 id="about">🧐 About</h2>

This is my first big Python project, which I put a lot of effort into, hope you get the most out of it :)

I used it to sell bible verse videos on Fiverr for a while.


<h2 id="working">💭 How it works</h2>

<h4>#1 Content</h4>
I got a 50+ stock background video (of mainly nature), 40 audio files and 10 fonts.

<h4>#2 Editing</h4>
The script works by taking a background video from '/videos', an audio file from '/audios', a random font, and a quote (a bible verse) from the JSON file, and combining them all into 1 video.

I am using **PILLOW** to generate the text in different fonts and **FFMPEG** to combine them all as fast as possible (I used **MoviePy** at the beginning but it was too slow).

All the video files and audio files are copyright-free from stock footage websites (Pexels, Pixabay, etc.), and the fonts are copyright-free as well.

<h2 id="how_to">🏁 How to run</h2>

Follow the instructions given below to get this script up and running on your device.

1. Download this repository as zip file / using git.
2. Open the folder.
3. Make sure all the required modules are installed. (`pip install -r requirements.txt`)
4. Open main.py
5. set the number of videos you want, your logo, and choose a quote file from '/sources/verses_data' (you can also use the <a href="https://github.com/SamuraiPolix/openbible-verse-scraper">topical bible verses scraper</a> I developed)
```python
number_of_videos = 99
customer_name = "your_name"
image_file = f"{project_dir}/sources/logo.png"
json_file = f"{project_dir}/sources/verses_data/love_data.json"
```
6. RUN!
7. And that's it! Everything else will be handled automatically!
8. You can find your video in the `customers/your-name/` directory.

<h2 id="built_using">⛏️ Built Using</h2>

1. [PILLOW](https://pypi.org/project/Pillow/) - For generating text images.
2. [FFMPEG](https://ffmpeg.org/) - For video editing.


<h2 id="results">🎥 Final Results</h2>

After running the script you will get these 3 files:
1. The edited video file.

   https://github.com/SamuraiPolix/ShortsMaker/assets/52662032/1640ba4f-13c5-4698-9f2f-bcbfacb9b908
3. A spreadsheet containing all the File names, verses, and references, to make it easier to find the video you want.

   ![image](https://github.com/SamuraiPolix/ShortsMaker/assets/52662032/6b597a1a-d7e0-495b-8f65-b6852eeb04a1)
4. The generated text image (for the quote in the video).

   <img src="https://github.com/SamuraiPolix/ShortsMaker/assets/52662032/340d9401-5aac-49f9-bf44-66e982b61abc" width="45%">

<h2 id="note">🗒️ Note</h2>

Note that this script is very basic as of now. I added **Text-to-Speak** in a later version which I will hopefully post soon. If you want to contribute, you are free to do so and you may even fork and improve this repository.
