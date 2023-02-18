```
    ____                  __         ____        __           _____            __                     
   / __ \____ _____  ____/ /___ _   / __ \____ _/ /_____ _   / ___/__  _______/ /____  ____ ___  _____
  / /_/ / __ `/ __ \/ __  / __ `/  / / / / __ `/ __/ __ `/   \__ \/ / / / ___/ __/ _ \/ __ `__ \/ ___/
 / ____/ /_/ / / / / /_/ / /_/ /  / /_/ / /_/ / /_/ /_/ /   ___/ / /_/ (__  ) /_/  __/ / / / / (__  ) 
/_/    \__,_/_/ /_/\__,_/\__,_/  /_____/\__,_/\__/\__,_/   /____/\__, /____/\__/\___/_/ /_/ /_/____/  
                                                                /____/                                
```
# Patch Feb 2023:
if your YouTube downloader/downloaders are failing:

Go here:

```
/usr/local/lib/python3.6/site-packages/youtube_dl/extractor/
```
search for the uploader id array:

old code:
```
'uploader_id': self._search_regex(r'/(?:channel|user)/([^/?&#]+)', owner_profile_url, 'uploader id') if owner_profile_url else None,
```
Replace with
```
'uploader_id': self._search_regex(r'/(?:channel/|user/|@)([^/?&#]+)', owner_profile_url, 'uploader id', default=None),
```

# Video-DL
Downloads video and audio at best quality from youtube and saves it as a mp4 file with the thumbnail as a jpg file in the same directory as the script.

# Requirements:
ffmpeg-python
```
pip3 install ffmpeg-python
```
pafy
```
pip3 install pafy
```
wget
```
pip3 install wget
```
youtube-dl
```
pip3 install youtube-dl
```

