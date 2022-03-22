
from typing import List
from Functions import Func2D as func
import sympy as sp
import numpy as np
import matplotlib as mp
import pandas as pd
from sympy import expand, re, im, I, E, symbols
import matplotlib.pyplot as plt


class FourierSeries():
    def __init__(self, Boundaries = [-1*np.pi,np.pi]):
        self.Boundaries = Boundaries
        pass


    def SymbolicSeries(self, Expression, NumberofTerms=5):
        x = sp.symbols('x')
        i = sp.symbols('i')
        Length = self.Boundaries[1] - self.Boundaries[0]
        Norm   = 2/Length
        Constants = {'A': [],'B': []}
        A0 = Norm * (sp.integrate(Expression, x).evalf(subs={x: self.Boundaries[1]}) - sp.integrate(Expression, x).evalf(subs={x: self.Boundaries[0]}))
        self.FourierSeriesExpression = A0/2
        Ai,Bi = self.SymbolicGeneralizeSeries(Expression)
        j = 1
        while j<= NumberofTerms:
            Constants['A'].append(Ai.evalf(subs={i: j}))
            Constants['B'].append(Bi.evalf(subs={i: j}))
            j += 1

        i = 0
        while i < NumberofTerms:
            self.FourierSeriesExpression = self.FourierSeriesExpression + Constants['B'][i]* sp.sin((i+1) * 2 * sp.pi * x/Length) + Constants['A'][i]* sp.cos((i+1) * 2 * sp.pi * x/Length)
            i = i+1
        self.FourierSeriesExpressionLatex = sp.latex(self.FourierSeriesExpression)

    def SymbolicGeneralizeSeries(self,Expression):
        i = sp.symbols('i')
        x = sp.symbols('x')
        Length = self.Boundaries[1] - self.Boundaries[0]
        Norm   = 2/Length
        Ai = Norm * (sp.integrate(Expression*sp.cos(i * 2 * sp.pi * x/Length),x).evalf(subs={x: self.Boundaries[1]}) - sp.integrate(Expression*sp.cos(i * 2 * sp.pi * x/Length),x).evalf(subs={x: self.Boundaries[0]}))
        Bi = Norm * (sp.integrate(Expression*sp.sin(i * 2 * sp.pi * x/Length),x).evalf(subs={x: self.Boundaries[1]}) - sp.integrate(Expression*sp.sin(i * 2 * sp.pi * x/Length),x).evalf(subs={x: self.Boundaries[0]}))
            
        return Ai,Bi

class FourierTransform:
    def __init__(self):
        self.UseasObject =True
        pass

    def SymbolicFT(self,Expression):
        omega = sp.symbols('omega')
        x     = sp.symbols('x')
        self.TransformedSymbolic = sp.fourier_transform(Expression, x, omega)
        self.TransformedSymbolicLatex = sp.latex(self.TransformedSymbolic)

    def SymbolicFTInverse(self,Expression):
        omega = sp.symbols('omega')
        x     = sp.symbols('x')
        self.TransformedSymbolicInversed = sp.inverse_fourier_transform(Expression,omega,x)
        self.TransformedSymbolicInversedLatex = sp.latex(self.TransformedSymbolicInversed)

class DiscreteFourierTransform:
    def __init__(self, Samplerate: int):
        self.Samplerate = Samplerate
        self.FundamentalExponent = np.exp(-1j * 2 * np.pi / self.Samplerate)
        J,K = np.meshgrid(np.arange(self.Samplerate),np.arange(self.Samplerate))
        self.DFTMatrix = np.power(self.FundamentalExponent,J*K)
        # print(self.DFTMatrix)
    
    def NumericDFT(self,Samples: List):
        self.Samples = Samples
        self.DFTFrequencies = np.matmul(self.DFTMatrix , (np.transpose(self.Samples)))
class FastFourierTransform:
    def __init__(self,Samplerate:int,Samples):
        self.Samplerate = Samplerate
        self.Sameples = Samples
        self.FFTFrequencies = np.fft.fft(Samples,Samplerate)

        
        


'''        

functionFourier = FourierSeries([-1,1])
functionFourier.SymbolicSeries(function.SymbolicTerm,10)
print(functionFourier.FourierSeriesExpressionLatex)

function = func('x')
function.Symbolic('sp.cos(x)')
function.TurnNumeric(5,3,[0,1])
function.NumericTerm['y']
DFTCalc = DiscreteFourierTransform(5)
DFTCalc.NumericDFT(function.NumericTerm['y'][0])


function = func('x')
function.Symbolic('sp.cos(x)+x**2')
expandFou = FourierSeries([-1,1])
expandFou.SymbolicSeries(function.SymbolicTerm,5)
print(expandFou.FourierSeriesExpressionLatex)
print(function.SymbolicTerm)

'''