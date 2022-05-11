# FFT research
![image](./cover.jpg)
In this repo I will gather codes and samples of Fast Fourier Transform for data manipulation using python and C++.

# Libraries
## Function.py
In this file we have the class responsible for creating a mathematical function generally using numpy or a numerical set of coordinates
### Example
```python 
# Example 1.1 | Sine function
sin = func2D(Numpy= 'a*np.sin(b*x)', Symbols='x,a,b') # Defining
y0  = sin.NumpyTerm(np.pi/2,3,1) # Since Numpy Term is a python function you can set inputs and 
                                 # Numerical outputs based on Symbols you defined 
print(y0)
# ------------------------------------------------
# Example 1.2 | A Numeric Function
Coordinates = {'x': [
    1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25
], 'y': [
    2,3,4,5,1,1,6,3,7,8,1,3,5,6,4,2,4,7,5,8,3,4,6,7,3
]}
num = func2D(Numeric = Coordinates) # Defining

# Let's plot and see
fig, ax = plt.subplots(figsize=(12,3))
ax.plot(num.NumericTerm['x'], num.NumericTerm['y'])

# ------------------------------------------------
# Example 1.3 | Importing CSV file
csv = func2D()
csv.ImportFromCSV('./data.csv',['x','y'])

fig, ax = plt.subplots(figsize=(12,3))
ax.plot(csv.NumericTerm['x'], csv.NumericTerm['y']) # Which is the ugly image below XD 
# since it's not one to one corresponding.
```
### Turning Numpy Terms Numerically
```python
# Example 2.1 | sine function numerical
xSample = func2D.LinearSampleMaker([-np.pi,np.pi], 44100) # We are making a sample of 44100 points 
                                                          # between -pi to pi.
sin.TurnNumpyNumeric(xSample, Symbols="5,2")

fig, ax = plt.subplots(figsize=(40,15))
plt.grid(True)
ax.plot(sin.NumericTerm['x'], sin.NumericTerm['y'], marker='o', ms=0.2, linestyle='None', c='darkblue')
ax.plot(sin.NumericTerm['x'], sin.NumericTerm['y']) # Which is the ugly image below XD 
# since it's not one to one corresponding.

# ------------------------------------------
# Example 2.2 | More complicated function
func = func2D(Numpy='np.sin(a*x**2)+b*np.cos(x**3)+c* np.cos(x*(-2))', Symbols='x,a,b,c')
xSample = func2D.LinearSampleMaker([0,2*np.pi], 44100) # We are making a sample of 44100 points 
                                                          # between -pi to pi.
func.TurnNumpyNumeric(xSample, Symbols="5,2,3")
fig, ax = plt.subplots(figsize=(40,20))

plt.grid(True)
ax.plot(func.NumericTerm['x'], func.NumericTerm['y'], marker='o', ms=0.2, linestyle='None', c='darkblue')
ax.plot(func.NumericTerm['x'], func.NumericTerm['y']) # Which is the ugly image below XD 
# since it's not one to one corresponding.
```

## Signal.py
```python
# Example 1.1 | sine signal
signal1 = Signal(44100, Numpy='np.sin(x)', Symbols='x')
#Example 1.2 | sine + cosine with different phase signal
signal2 = Signal(44100, Numpy='np.sin(a*x)+np.cos(b*x)', Symbols='x,a,b')
# --------------------------------------------
# Example 1.1 | sine signal
signal1.SampleMaker([0,2*np.pi], '', 1) # from 0 to 2pi, length 1 second.
#Example 1.2 | sine + cosine with different phase signal
signal2.SampleMaker([0,2*np.pi], '2,3', 0.1)# from 0 to 2pi with a=2,b=3 and for length 1 second.
```

## Processing.py
In this file we have fft rfft and other needed tools to process signals

## Generators.py
Needed methods to develop the processings etc...

## Links
[Notion](https://thisismeamir.notion.site/Fast-Fourier-Transform-8225af529e3643168e811751ff88c8cf)
