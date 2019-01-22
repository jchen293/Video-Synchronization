#get audio from video
import subprocess


class VidToAud:
    def __init__(self, input_path, output_path):# reference video name and comparison video name
        self.video_in = input_path
        self.video_out = output_path

    def extract_audio(self):
        subprocess.call(['ffmpeg', '-i', self.video_in, '-vcodec', 'copy', '-vn', self.video_out])
        return True
