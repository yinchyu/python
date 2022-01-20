import numpy as np
import wave


def my_ispeech( chunk,silent_threshold=0.007,ap=0.8):
    '''
    energy1 是另一种静音的检测方式， energy2是能量的检测方式，使用engrey2 来进行静音检测
    sil_detector =SilenceDetector(105)
    energy1, isspeech1 = sil_detector.is_silence(chunk)
    return energy > silent_threshold
    :param chunk:
    :return:
    '''
    energy2 = sum([abs(sample / 32768.0) for sample in chunk]) / len(chunk)
    print("++++++++++ ", "{:4f}".format(energy2*ap), silent_threshold, energy2*ap > silent_threshold,
              " ++++++++++")
    # return energy2 > silent_threshold
from scipy.io import wavfile
npdata=wavfile.read("s11.wav")[1]
for i in range(0,len(npdata),160):
    my_ispeech(npdata[i:i+160])
    # print(np.mean(npdata[1])/32768.0,np.max(npdata[1])/32768.0,np.min(npdata[1])/32768.0)