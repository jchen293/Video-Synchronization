import subprocess


class VidList:
    def __init__(self, obj_num, video_path):
        self.video_path = video_path
        self.target = self.video_path + '*{0:03d}*.mp4'.format(obj_num)

    def extract_video_list(self, txt_file):
        # add '/s' will include the whole path of file
        subprocess.call(['dir', '/b', self.target, '>', self.video_path + txt_file], shell=True)
        return True

    def get_file_name(self, txt_file):
        content = open(self.video_path + txt_file)
        file_list = content.read().split('\n')
        file_list = file_list[0:len(file_list)-1]
        content.close()
        return file_list

