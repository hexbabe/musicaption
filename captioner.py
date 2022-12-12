import json
from moviepy.editor import *
from moviepy.video.tools.subtitles import SubtitlesClip

def caption_video(video_path, subtitle_data):
    generator = lambda txt: TextClip(txt, font='Georgia-Bold', fontsize=88, color='white')
    subtitles = SubtitlesClip(subtitle_data, generator)

    video = VideoFileClip(video_path)
    result = CompositeVideoClip([video, subtitles.set_pos(('center'))])

    result_path = f'outputs/captioned_{os.path.basename(video_path)}'
    result.write_videofile(result_path, fps=video.fps, temp_audiofile="temp-audio.m4a", remove_temp=True, codec="libx264", audio_codec="aac")

if __name__ == '__main__':
    video_file_name = input('Verify subs.json is okay, then give video file name (exclude ext): ')
    with open('./subs.json', 'r') as f:
        subtitle_data = json.load(f)
    caption_video(f'inputs/videos/{video_file_name}.mov', subtitle_data)