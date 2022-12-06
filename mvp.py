from transcriber import transcribe_to_subs
from captioner import caption_video

if __name__ == '__main__':
    audio_file_name = input('Audio file name (exclude ext): ')
    video_file_name = input('Video file name (exclude ext): ')

    subs = transcribe_to_subs(f'inputs/audios/{audio_file_name}.wav')
    caption_video(f'inputs/videos/{video_file_name}.mp4', subs)