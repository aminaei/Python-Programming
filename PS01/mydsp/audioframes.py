"""

  Due Date: September 19, 2017

  Code: audioframes.py
  Created by: Ali Minaei

"""

import scipy.io.wavfile as wavfile
import numpy as np

class AudioFrames:
    """AudioFrames
    A class for iterating over frames of audio data
    """

    def __init__(self, filename, adv_ms, len_ms):
        # AudioFrames(filename, adv_ms, len_ms)
        # Create a frame generator from file filename where each is
        # len_ms milliseconds long and frames are advanced by adv_ms.

        self.filename = filename
        self.adv_ms = adv_ms
        self.len_ms = len_ms

        # scipy.io.wavfile.read('wave filename')
        #
        # returns:
        # rate : (int) -- Sample rate of wav file (in samples/sec)
        # data : (numpy array) -- Data read from wav file

        self.rate, self.data = wavfile.read('./talking.wav')
        self.data = self.data.astype(np.int64)

        # frame length in samples (samples) = sample rate(samples/sec) * frame length (msec) * 1sec/1000msec
        self.framelen_samples = int(np.round(self.rate * (self.len_ms / 1000.0)))
        self.frameadv_samples = self.framelen_samples/2

        # print("Number of data points = ", len(self.data))
        # print("Number of samples in the Frame length ", self.framelen_samples)
        # print("Number of Advance samples in the Frame length ", self.frameadv_samples)

        self.frametotal = int(round(len(self.data)/self.frameadv_samples))
        self.index = self.frametotal + 1



    # get_framelen_samples() - Return frame length in samples
    def get_framelen_samples(self):
        # frame length in samples (samples) = sample rate(samples/sec) * frame length (msec) * 1sec/1000msec

        return self.framelen_samples

    # get_framelen_ms() - Return frame length in ms
    def get_framelen_ms(self):
        return self.len_ms

    # get_frameadv_samples() - Return frame advance in samples
    def get_frameadv_samples(self):

        return self.frameadv_samples

    # get_frameadv_ms - Return frame advance in ms
    def get_frameadv_ms(self):

        return self.adv_ms

    # get_Fs() - Return sample rate
    def get_Fs(self):
        return self.rate

    # __iter__() - return iterator
    def __iter__(self):

        return self

    # __next__() - return next frame
    def __next__(self):
        if self.index == 0:
            raise StopIteration

        self.index = self.index - 1

        i = int((self.frametotal-self.index)*self.frameadv_samples)
        j = int(i + self.framelen_samples)
        # print("--> AudioFrames : i = ",i," j = ",j)

        return self.data[i:j]

