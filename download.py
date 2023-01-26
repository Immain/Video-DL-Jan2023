import pafy
import re
import wget

url = "https://youtu.be/S2k99-bopIc"

exp = "^.*((youtu.be\/)|(v\/)|(\/u\/\w\/)|(embed\/)|(watch\?))\??v?=?([^#&?]*).*"
s = re.findall(exp,url)[0][-1]
thumbnail = f"https://i.ytimg.com/vi/{s}/maxresdefault.jpg"
wget.download(thumbnail)
print(thumbnail)

result = pafy.new(url)

streams = result.streams
for stream in streams:
    print(stream)

best_quality_video = result.getbestvideo(preftype="mp4")

print(best_quality_video)

best_quality_video.download()
