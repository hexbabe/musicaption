import os
import glob
from pydub import AudioSegment
import moviepy.editor as moviepy

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

def convert_all_movs_to_mp4s():
    extension_list = ('*.MOV', '*.mov', '*.m4v')
    converted_files = []
    for extension in extension_list:
        for video in glob.glob(extension):
            filename_no_ext = os.path.splitext(os.path.basename(video))[0]
            clip = moviepy.VideoFileClip(os.path.basename(video), target_resolution=(1080, 1920))
            clip.write_videofile(filename_no_ext + '.mp4')
            clip.close()
            # keep track of converted files
            converted_files.append(filename_no_ext + '.mp4')
    return converted_files
    



if __name__ == '__main__':
    os.chdir('inputs/audios')
    print(convert_all_audios_to_wavs())
    os.chdir('../videos')
    print(convert_all_movs_to_mp4s())
