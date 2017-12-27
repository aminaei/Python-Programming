"""


  Due Date: September 19, 2017

  Code: rmsstream.py
  Created by: Ali Minaei

"""
from numpy import mean, sqrt, square

class RMSStream:

    def __init__(self, frame_stream):
        """"RMSStream(frame_stream) - Initialize a root mean square stream
        from an instance of AudioFrames.
        """
        self.frame_stream = frame_stream
        # self.rms = sqrt(mean(square(self.frame_stream)))
        # self.index = self.frame_stream.__len__()

        # for data in self.frame_stream:
        #     self.rms = sqrt(mean(square(data)))
        #     self.index = self.index + 1

        # print("RMSStream: index = ",self.index)
        i = 0
        self.rms = []
        for data in self.frame_stream:
            self.rms.append(sqrt(mean(square(data,dtype='int64'))))

        self.index = -1
        self.rms_size = len(self.rms)


        # print("--> RMSStream: index = ",self.index)


        # print("--> RMSStream: rms_size = ",self.rms_size)
        # print("--> RMSStream: rms = ",self.rms)



    def __iter__(self):
        "__iter__() - return iterator"
        return self

    # next - next RMS value
    def __next__(self):
        self.index = self.index + 1

        if self.index > self.rms_size-1:
            raise StopIteration

        return self.rms[self.index]

