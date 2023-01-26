import pafy
import re
import wget
import string
import random
import os

url = "https://www.youtube.com/watch?v=NkRkuI0ZgX0"

exp = "^.*((youtu.be\/)|(v\/)|(\/u\/\w\/)|(embed\/)|(watch\?))\??v?=?([^#&?]*).*"
s = re.findall(exp,url)[0][-1]
letters = string.ascii_uppercase
thumbnail = f"https://i.ytimg.com/vi/{s}/maxresdefault.jpg"
file = f"{s}-{( ''.join(random.choice(letters) for i in range(10)) )}.jpg"
wget.download(thumbnail)
os.rename("maxresdefault.jpg", file)
print(thumbnail)

result = pafy.new(url)

streams = result.streams
for stream in streams:
    print(stream)

best_quality_video = result.getbestvideo(preftype="mp4")

print(best_quality_video)

best_quality_video.download()

