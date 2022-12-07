# musicaption

I hate subtitling my music videos on TikTok, Reels, and YouTube. This allows me and others to auto-caption their music videos
using the original video plus an audio recording of their voice speaking the words of the song

# Thoughts

For the MVP I'm using an offline speech recognition model from Vosk and MoviePY for subtitles.

Vosk generates a JSON "transcript" containing objects with the words and their time bounds in the audio.

Fortunately, subtitles use text + time bounds— go figure. Pass those into MoviePY and voila

If you want to run this WIP MVP:
1. Set up your Python venv and install the requirements
2. Install/make sure FFMPEG is installed on your system
3. Download the vosk-model-en-us-0.22 language model from the Vosk website and unzip the folder in the outermost repo directory
4. Run mvp.py, giving 'h4t' as the two inputs when prompted to caption the default inputs in the folder
5. Repeat with your own synced voice + video inputs
