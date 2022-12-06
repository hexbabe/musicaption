from moviepy.editor import *
from moviepy.video.tools.subtitles import SubtitlesClip

def caption_video(video_path, subs):
    generator = lambda txt: TextClip(txt, font='Georgia-Bold', fontsize=50, color='white')
    subtitles = SubtitlesClip(subs, generator)

    video = VideoFileClip(video_path)
    result = CompositeVideoClip([video, subtitles.set_pos(('center'))])

    result_path = f'outputs/captioned_{os.path.basename(video_path)}'
    result.write_videofile(result_path, fps=video.fps, temp_audiofile="temp-audio.m4a", remove_temp=True, codec="libx264", audio_codec="aac")