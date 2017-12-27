'''
Created on Sep 11, 2017

@author: mroch

How to use this:
Place in any directory outside of the code that you will be submitting
Place a copy of talking.wav in the same directory
Run it as follows:  
    python tester.py path/to/assingment1_files
    
Note that as-is, this will not test the correctness of your code,
only some of the interfaces and ensures that your code can be accessed with
the exception of your main module driver.py that should be in:
    path/to/assignment1_files/driver.py

For your debugging, you may wish to write out a wave file that has
integer values in sequence 1, 2, 3, ...  It makes it easier to see if
you are doing the framing correctly.

'''
import unittest
import os.path
import sys


import numpy as np
import matplotlib.pyplot as plt

from matplotlib.pyplot import plotting


# Set up import paths
if __name__ == '__main__':    
    
    # first argument is user's directory, get it & validate
    try:
        # Grab the argument and remove it.  If not removed,
        # the unittest framework will try to parse it
        user_dir = sys.argv[1]
        del sys.argv[1]
    except IndexError:
        raise ValueError("Must provide user directory")
    if not os.path.isdir(user_dir):
        raise ValueError("{} is not a directory".format(user_dir))
    
    sys.path.append(user_dir)

# Import student code
# A code analysis tool like pydev will probably mark these as
# unresolved imports as they won't be accessible until you the
# search path is modified at run time.
from mydsp.audioframes import AudioFrames
from mydsp.rmsstream import RMSStream
import mydsp.plots as plots


class TestAudio(unittest.TestCase):
    
    
    def checkAudioFrames(self, filename, adv_ms = 10, len_ms = 20):
        """checkAudioFrames(filename, adv_ms, len_ms)
        check framing with specified parameters
        """
                   
        print("\nVerifying framing  adv_ms {} len_ms {}".format(
            adv_ms, len_ms))
            
        success = True # declare victory until we fall on our face...
    
        framer = AudioFrames(filename, adv_ms, len_ms)
        
        # Check if works...
        
        return success
    
    def test_AudioFrames(self):
        return self.checkAudioFrames("talking.wav", 10, 20)
    
    def test_RMS(self):
        
        # set up the energy streamer
        framer = AudioFrames("talking.wav", 10, 20)
        energy = RMSStream(framer)
        
        success = True  # victory (we hope)
        
        # run tests...
        
        return success
    
    
        
    
if __name__ == '__main__':    
    plt.ion()  # Turn on interactive plotting
    unittest.main()