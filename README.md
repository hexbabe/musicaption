# musicaption

I hate subtitling my music videos on TikTok, Reels, and YouTube. This allows me and others to auto-caption their music videos

# Thoughts

For the MVP I'm using an offline speech recognition model from Vosk and MoviePY for subtitles.

Vosk generates a JSON "transcript" containing objects with the words and their time bounds in the audio.

Fortunately, subtitles use text + time bounds— go figure. Pass those into MoviePY and voila
