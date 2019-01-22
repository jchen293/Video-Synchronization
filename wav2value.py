from scipy.io.wavfile import read
import matplotlib.pyplot as plt


class Wav2Value:
    def __init__(self, wav_file):
        self.wav_file = wav_file
        print(wav_file)

    def get_wav_para(self):
        rate, data = read(self.wav_file)
        return rate, data

    def plot_wav(self, channel_num):
        rate, data = self.get_wav_para()
        plt.plot(data[:, channel_num])
        plt.ylabel("Amplitude")
        plt.xlabel("Time")
        plt.title("wav plot of channel {0:01d}".format(channel_num))
        plt.show()
