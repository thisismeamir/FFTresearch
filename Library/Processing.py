import scipy  as sc
import numpy as np
import matplotlib as mp
import matplotlib.pyplot as plt
from scipy.fft import fft, fftfreq, rfft, rfftfreq
from Library.Function import func2D as func


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


class GeoProcess():
    @staticmethod
    def Maxmin(Range=int, Steps=int, data = func):
        '''
        Given a Range and a step this functions finds the difference between maximum and minimum value inside a range 
        using the steps we determine on how many itteration we want to sweep whole datas.
        '''
        datalen = len(data.NumericTerm['x'])
        rate = datalen//Steps
        walk = Range
        Deltas = []
        WalkRange = []
        Key = False
        while walk <= datalen:
            max = np.max(data.NumericTerm['x'][0:walk])
            min = np.min(data.NumericTerm['x'][0:walk])
            delta = max - min 
            Deltas.append(delta)
            WalkRange.append(walk)
            walk += rate
            if walk >= datalen and Key == False:
                walk = datalen
                Key = True
            else:
                continue
        
        Dataexport = {'Walkrange': WalkRange, 'Deltas': Deltas}
        return Dataexport
