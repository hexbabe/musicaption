# import os
# from moviepy import editor

# def _caption_clip(clip, txt, txt_color='white', fontsize=50, font='Georgia-Bold'):
#     """ Writes text to the center of the clip. """
#     text_clip = editor.TextClip(txt, fontsize=fontsize, font=font, color=txt_color)
#     cvc = editor.CompositeVideoClip([clip, text_clip.set_pos(('center'))])
#     return cvc.set_duration(clip.duration)

# def caption_video(video_path, subs):
#     video = editor.VideoFileClip(video_path)
#     captioned_clips = [_caption_clip(video.subclip(from_t, to_t), txt) for (from_t, to_t), txt in subs]
#     captioned_video = editor.concatenate_videoclips(captioned_clips)
#     video_resized = captioned_video.resize((1920, 1080))
#     video_resized.write_videofile(f'outputs/captioned_{os.path.basename(video_path)}')


from moviepy.editor import *
from moviepy.video.tools.subtitles import SubtitlesClip

def caption_video(video_path, subs):
    generator = lambda txt: TextClip(txt, font='Georgia-Bold', fontsize=50, color='white')
    subtitles = SubtitlesClip(subs, generator)

    video = VideoFileClip(video_path)
    result = CompositeVideoClip([video, subtitles.set_pos(('center'))])

    result_path = f'outputs/captioned_{os.path.basename(video_path)}'
    result.write_videofile(result_path, fps=video.fps, temp_audiofile="temp-audio.m4a", remove_temp=True, codec="libx264", audio_codec="aac")