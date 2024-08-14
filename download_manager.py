import os
from pytubefix import YouTube
from moviepy.editor import VideoFileClip, AudioFileClip
from datetime import datetime


class DownloadManager:
    def __init__(self, save_path):
        self.save_path = save_path

    def download_video(self, url):
        yt = YouTube(url)
        video_filename = datetime.now().strftime("%Y_%m_%d_%H_%M_%S") + ".mp4"
        video_path = os.path.join(self.save_path, "video")
        os.makedirs(video_path, exist_ok=True)
        yt.streams.filter(only_video=True).first().download(
            output_path=video_path, filename=video_filename
        )
        return os.path.join(video_path, video_filename)

    def download_audio(self, url):
        yt = YouTube(url)
        audio_filename = datetime.now().strftime("%Y_%m_%d_%H_%M_%S") + ".mp3"
        audio_path = os.path.join(self.save_path, "audio")
        os.makedirs(audio_path, exist_ok=True)
        yt.streams.filter(only_audio=True).first().download(
            output_path=audio_path, filename=audio_filename
        )
        return os.path.join(audio_path, audio_filename)

    def merge_video_audio(self, video_path, audio_path):
        video_clip = VideoFileClip(video_path)
        audio_clip = AudioFileClip(audio_path)
        video_clip = video_clip.set_audio(audio_clip)

        output_path = os.path.join(
            self.save_path, f"{datetime.now().strftime('%Y_%m_%d_%H_%M_%S')}_merged.mp4"
        )
        video_clip.write_videofile(output_path, codec="libx264", audio_codec="aac")
