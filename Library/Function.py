import numpy as np
import scipy as sc
import pandas as pd

'''
We first define a class of mathematical functions.
Symbolic functions are not yet implemented...
'''

class func2D():
    '''
    Class of mathematical Functions.
    '''
    def __init__(self, Numpy = "", Numeric = "", Symbols = ""):
        '''
        This method is the initial function for making a 2D mathematical function.
        First define Symbols in your function and then,
        you can use self.Numpy('Numpy expression: np.cos(x)') 
        or          self.Numeric ({"x": [], "y": []})
        to define the function in terms of coordinate numbers or symbolic term
        '''
        
        if Numpy != "":
            self.Numpy(Numpy,Symbols)
        elif Numeric != "":
            self.Numeric(Numeric)
        else:
            pass

    # ---------- Defining Methods ----------
    def Numpy(self, Expression, Symbols):
        '''
        This method gets a numpy function as a string and turns it to actual numpy function.
        '''

        Define = "lambda" + " " + Symbols + " :"
        exec('self.NumpyTerm = {0} {1}'.format(Define, Expression))
    
    def Numeric(self, Numeric):
        '''
        This method is resposible for recieving a set of coordinates and the coresponding value of the function.
        {'x': [1,3,4,5,6,7,8,15,17,18,100,230,...],
         'y': [13,15,1,6,4,52,37,37,563,6,745,...]}
         the lengths of 'x' and  'y' lists have to be equal. 
        '''
        assert len(Numeric['x']) == len(Numeric['y']), 'The two given lists are not equal'
        
        self.NumericTerm = Numeric
    
    # ---------- Turning Numeric ----------
    def TurnNumpyNumeric(self, Sample, Symbols="", Signal = False):
        '''
        Turns Numpy Expressions into Numeric functions.
        '''
        self.SampleLength = len(Sample)
        self.SampleRate   = self.SampleLength//self.SampleDuration
        Sample = Sample
        y =[]
        if Symbols == "":
            for x in Sample:
                Eval = self.NumpyTerm(x)
                y.append(Eval)
        else:
            for x in Sample:
                # Eval = 0
                Eval = eval("self.NumpyTerm({0},{1})".format(x,Symbols))
                y.append(Eval)
        if Signal:
            return {'x': Sample, 'y': np.array(y)}
        else:
            self.NumericTerm = {'x': Sample, 'y': np.array(y)}


    def ImportFromCSV(self,path, columns =['','']):
        '''Importing Numeric Values from a CSV file.'''
        df = pd.read_csv(path, skipinitialspace=True)
        x = np.transpose(df[columns[0]].to_numpy())
        y = np.transpose(df[columns[1]].to_numpy())
        self.NumericTerm = {'x': x, 'y': y}
    
    # ---------- Status ----------    
    def Ready(self,Stateof):
        '''
        Finding if an instance has symbolic,numeric,numpy expressions
        '''
        assert Stateof in ["Num", "Numpy"],'The argument should be "Num", "Numpy"'
        PossibleTerms = ["Num","Numpy"]
        terms= {"Num": self.NumericTerm, "Numpy": self.NumpyTerm}
        for term in PossibleTerms:
            if term == Stateof:
                if terms[term]!= "":
                    return True
                else:
                    return False
            else:
                return "Not Found."
        
