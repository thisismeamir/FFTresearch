from sre_parse import State
import numpy as np
import sympy as sp
import matplotlib as mp
import pandas as pd
from sympy import re, im, I, E, symbols

# Plotting
from sympy.plotting import plot 
from sympy.plotting import plot3d
from sympy.plotting import plot_parametric
from sympy.plotting import plot3d_parametric_line
from sympy.plotting import plot3d_parametric_surface

class Func2D:
    def __init__(self, Symbols):
        '''
        This method is the initial function for making a 2D mathematical function.
        you can use self.Symbolic('Latex expression') 
        or          self.Numeric ({"x": [], "y": []})
        to define the function in terms of coordinate numbers or symbolic term
        '''

        # Truning String of multiple symbols into sp.symbol() functions
        Symbols = Symbols.split(' ')
        self.Symbols = []
        for Symbol in Symbols:
            exec('self.{0} = sp.symbols("{0}")'.format(Symbol)) 
            self.Symbols.append(Symbol)



        self.LatexTerm    = ""
        self.SymbolicTerm = ""
        self.NumericTerm  = {'x':[],'y':[]}
    
    # These Two functions are used to Define a function symbolically or numerically.
    def Symbolic(self, Expression):
        '''
        This  method is responsible for recieving the latex expression for our function.
        self.Symbolic('Latex expression', 'Symbols').
        '''
        for Symbol in self.Symbols:
            exec('{0} = sp.symbols("{0}")'.format(Symbol))
        exec('self.SymbolicTerm = {0}'.format(Expression))
        self.LatexTerm = sp.latex(self.SymbolicTerm)
    
    def Numeric(self, Coordinates: dict):
        '''
        This method is resposible for recieving a set of coordinates and the coresponding value of the function.
        {'x': [1,3,4,5,6,7,8,15,17,18,100,230,...],
         'y': [13,15,1,6,4,52,37,37,563,6,745,...]}
         the lengths of 'x' and  'y' lists have to be equal. 
        '''
        assert len(Coordinates['x']) == len(Coordinates['y']), 'The two given lists are not equal'

        self.NumericTerm = Coordinates

    # Turning a Symbolic Function into Numeric values with a given Sample rate.
    def TurnNumeric(self,SampleRate=10, Precision=3, Range=[0,1]):
        self.SampleRate = SampleRate
        SampleRate = np.linspace(Range[0], Range[1], SampleRate)
        y = []
        for x in SampleRate:
            Eval = self.SymbolicTerm.evalf(subs={self.Symbols[0] : x})

            y.append(Eval)
        
        self.NumericTerm = {'x': SampleRate, 'y': np.array(y)}
    
    def ImportFromCSV(self,path, column):
        df = pd.read_csv(path, skipinitialspace=True, usecols=column)
        SampleRate = len(df.index)
        self.SampleRate = SampleRate
        y = np.transpose(df.to_numpy())
        self.NumericTerm = {'x': 0, 'y': y}



    def Ready(self,Stateof):
        assert Stateof in ["Num", "Sym", "NumSym"],'The argument should be "Num", "Sym", "NumSym"'
        if Stateof == "Num" and len(self.NumericTerm) == 2:
            return "NumericTrue"
        elif Stateof =="Num" and len(self.NumericTerm) !=2:
            return "NumericFalse"
        elif Stateof == "Sym" and self.SymbolicTerm != "":
            return "SymbolicTrue"
        elif Stateof == "Sym" and self.SymbolicTerm == "":
            return "SymbolicFalse"
        elif Stateof == "NumSym" and self.SymbolicTerm == "" and len(self.NumericTerm) != 2:
            return "NumericSymbolicTrue"
        else:
            return "NumericSymbolicFalse"
    
    
       

        
    
    
    # Plotting
    def Plot(self, keys=""):
        exec('plot(self.SymbolicTerm, {0})'.format(keys))
    
