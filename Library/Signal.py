from msilib.schema import File
from Function import func2D as func
import numpy as np
import scipy as sc
from scipy.io.wavfile import write 
from msilib.schema import File
import numpy as np
import scipy as sc
from scipy.io.wavfile import write 

class Signal(func):
    def __init__(self, SampleRate, Numpy="", Numeric="", Symbols="", ):
        '''
        Initial Signal Making.
        '''
        super().__init__(Numpy, Numeric, Symbols)
        self.SampleRate = SampleRate


    # ---------- Making a Sample from a Signal ----------
    def SampleMaker(self, Range: list, Constants='', Length = 1):
        '''
        Making a Sample from a given numpy signal
        '''
        assert len(Range) == 2, "Range should be in the form  [a,b]."
        self.SampleDuration = Length
        SampleNumber = int(self.SampleDuration * self.SampleRate)
        x = func.LinearSampleMaker(Range, SampleNumber)
        self.SignalSample = self.TurnNumpyNumeric(x, Constants, Signal = True)
        self.SignalSampleVar = self.SignalSample['x']
        self.SignalSample = self.SignalSample['y']
        self.Sampled = True
        
    def Normalizer(self, Amplitude = 1):
        '''
        Generalized Normalizer
        '''
        self.SignalSample = np.int16((self.SignalSample/self.SignalSample.max())*Amplitude)
    
    def NormalizerInt16(self):
        '''
        Normalizing the sample for audio making
        '''
        self.SignalSample = np.int16((self.SignalSample/self.SignalSample.max())*32767)

    # ---------- Audio ----------
    def NumericAudioCreator (self, Duration, FileName="wave"):
        '''
        Turning a Signal into audio.
        '''
        Repeat   = Duration//self.SampleDuration
        wave = np.array([])
        i = 0
        while i < Repeat:
            wave = np.concatenate((wave, self.SignalSample), axis=None)
            i +=1
        write(f"{FileName}.wav", self.SampleRate, wave)

    # ---------- Audio from Numpy ----------
    def NumpyAudioCreator (self, Duration, Range, Constants, Length, FileName="wave"):
        '''
        Turning a numpy term into audio.
        '''
        assert self.Ready('Numpy')
        self.SampleMaker(Range,Constants,Length)
        self.NumericAudioCreator(Duration, FileName)