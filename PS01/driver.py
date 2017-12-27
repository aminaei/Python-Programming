"""

  Due Date: September 19, 2017

  Code: driver.py
  Created by: Ali Minaei

"""

from mydsp.audioframes import AudioFrames
from mydsp.rmsstream import RMSStream
from mydsp.plots import plots

import numpy as np
import matplotlib.pyplot as plt


###################################################################################
def Main():

    # rate: (int) - - Sample rate of wavfile( in samples / sec)
    # data: (numpy array) -- Data read from wav file

    aframe = AudioFrames('./talking.wav',10,20)
    # print("Frame length samples = ", aframe.get_framelen_samples)
    rate = aframe.get_Fs()
    # data = aframe.get_data()
    print("sample rate = ",rate)
    # print("length of data = ",len(data),"\n\n")

    myrms =  RMSStream(aframe)

    rms_data = [i for i in myrms]
    print("rms_data len = ",len(rms_data))
    # print(rms_data)

    timeArray = np.arange(0, len(rms_data),1)*aframe.get_frameadv_ms()
    timeArray = timeArray / 1000
    # print("get_frameadv_ms = ",aframe.get_frameadv_ms())
    # print("timeArray len = ",len(timeArray))
    plt.figure(1)
    plt.plot(timeArray, 20*np.log10(rms_data))
    plt.ylabel('dB rel')
    plt.xlabel('Time (s)')
    plt.title('Pressure RMS vs Time')


    #
    frame_index = int((1.3/aframe.get_frameadv_ms())*1000)
    # print(" --> frame_index = ",frame_index)



    noise_data = rms_data[0:frame_index-1]
    speech_data = rms_data[frame_index:len(rms_data)-1]
    # print("len(speech_data) = ",len(speech_data)," len(noise_data) = ",len(noise_data))

    # print(speech_data)
    # conver RMS data to dB
    speech_data_db = 20*np.log10(speech_data)
    noise_data_db = 20*np.log10(noise_data)

    (speech_mean,speech_var) = plots.fit_norm(speech_data_db)
    (noise_mean,noise_var) = plots.fit_norm(noise_data_db)
    # print((speech_mean,speech_var))
    #
    # print("speech_mean = ",speech_mean," speech_var = ",speech_var)
    plots.plot_data(speech_data_db,speech_mean,speech_var)


    plots.plot_data(noise_data_db,noise_mean,noise_var)
    plt.show()

if __name__ == '__main__':
    Main()
