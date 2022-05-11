import scipy  as sc
import numpy as np
import matplotlib as mp
import matplotlib.pyplot as plt
from scipy.fft import fft, fftfreq, rfft, rfftfreq

class SignalProcessing():
    def __init__(self):
        pass

    @staticmethod
    def fft(SampleRate, Duration, Signal, key=""):
        '''
        Easy fft for signals!
        '''
        assert key in ['both', 'freq', ''], "key should be in ['both', 'freq', '']."
        SampleLength = SampleRate * Duration
        Amplitudes = fft(Signal)
        Frequencies = fftfreq(SampleLength,1/SampleRate)
        # Returns
        if key == 'both':
            return Amplitudes, Frequencies
        elif key =='freq':
            return Frequencies
        elif key =='':
            return Amplitudes
        else:
            pass

    @staticmethod
    def rfft(SampleRate, Duration, Signal, key=""):
        '''
        Easy fft for signals!
        '''
        assert key in ['both', 'freq', ''], "key should be in ['both', 'freq', '']."
        SampleLength = int(SampleRate * Duration)
        Amplitudes = rfft(Signal)
        Frequencies = rfftfreq(SampleRate,1/SampleRate)
        # Returns
        if key == 'both':
            return Amplitudes, Frequencies
        elif key =='freq':
            return Frequencies
        elif key =='':
            return Amplitudes
        else:
            pass