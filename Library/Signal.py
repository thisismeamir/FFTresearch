from msilib.schema import File
from Library.Function import func2D as func
import numpy as np
import scipy as sc
from Library.Generators import GeneralGenerators as gg
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
        x = gg.LinearSampleMaker(Range, SampleNumber)
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
        Normalizing the sample for audio making.
        '''
        self.SignalSample = np.int16((self.SignalSample/self.SignalSample.max())*32767)
   
    # ----------        Noising        ----------                                               
    def AddNoise(self, Range, std, Region='All'):
        '''
        Generates Noise to a Region of Data
        '''
        if Region == 'All':
            Noise = gg.GaussianNoise(Range, self.SignalSampleVar, std)
            self.SignalSampleNoised = self.SignalSample + Noise
        else:
            SampleVar = self.SignalSample[Region[0]*self.SampleRate:Region[1]*self.SampleRate]
            Noise = self.NoiseSample(Range, SampleVar, std)
            self.SignalSampleNoised = np.concatenate((self.SignalSample[0:Region[0]*self.SampleRate],
            self.SignalSample[Region[0]*self.SampleRate:Region[1]*self.SampleRate]+Noise))

                     
                                                    
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
