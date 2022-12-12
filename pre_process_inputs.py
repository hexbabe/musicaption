import os
import glob
from pydub import AudioSegment

def convert_all_audios_to_wavs():
    extension_list = ('*.mp3', '*.m4a')
    converted_files = []
    for extension in extension_list:
        for audio in glob.glob(extension):
            wav_filename = os.path.splitext(os.path.basename(audio))[0] + '.wav'
            AudioSegment.from_file(audio).export(wav_filename, format='wav')
            # keep track of converted files
            converted_files.append(wav_filename)
    return converted_files
    



if __name__ == '__main__':
    os.chdir('inputs/audios')
    print(convert_all_audios_to_wavs())
