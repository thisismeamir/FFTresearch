from numbers import Integral

from matplotlib.transforms import Transform
from Functions import Func2D as func
import sympy as sp
import numpy as np
import matplotlib as mp
import pandas as pd
from sympy import re, im, I, E, symbols

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

    def NumericFT(self,Numerics):
        pass
    def NumericFTInverse(self,Numerics):
        pass

        


'''        

functionFourier = FourierSeries([-1,1])
functionFourier.SymbolicSeries(function.SymbolicTerm,10)
print(functionFourier.FourierSeriesExpressionLatex)
'''
function = func('x')
function.Symbolic('sp.exp(-x**2)')
Ftrans = FourierTransform()
Ftrans.SymbolicFT(function.SymbolicTerm)
Ftrans.SymbolicFTInverse(Ftrans.TransformedSymbolic)
print(Ftrans.TransformedSymbolicLatex)
print(Ftrans.TransformedSymbolicInversedLatex)