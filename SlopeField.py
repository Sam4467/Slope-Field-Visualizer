import numpy as np
import matplotlib.pyplot as plt
from sympy import *

gradients = []                          # List to store all gradients of derivitive
grad2 = []                              # Secondary list to store normalized data

x, y = symbols('x y')                   # Declares variables used in function
f = eval(input("Enter function: "))     # Asks for mathematical function to create slope field of
if 'y' in str(f):                       # Checks if the function is multivariable
    df = 1/idiff(f, x, y)               # Uses implicit differentiation 
else:                       
    df = diff(f, x)                     # Uses standard differentiation
print("Derivitive Function:", df)
for X in range(-5, 6, 1):               # For all points across the x and y axis
    for Y in range(-5, 6, 1):       
        if 'y' in str(f):               # Checks if derivitive is in terms of y and multivariable
            if 'x' in str(f):       
                m = df.subs([(x,X), (y,Y)]) # Solve gradients for each (x,y) point
            else:                 
                m = df.subs(y,Y)
        else:
            m = df.subs(x,X)
        try:
            m = float(m)            # Converts all gradients to a float (from fraction)
        except:
            m = 0                   # If value is nan or infinite it gets set to 0 
        gradients.append(m)         # adds each gradients to list

X, Y = np.meshgrid(np.arange(-5, 6, 1), np.arange(-5, 6, 1))        # Creates a meshgrid from (-5,-5) to (5,5)
u = np.ones((11,11))             # Creates 2D array of ones to be a placeholder in the quiver function
for m in gradients:
    n = np.sqrt(m**2+1)          # Normalize data
    m_norm = m/n
    grad2.append(m_norm)
plt.quiver(Y, X, u, grad2,  headlength = 0, pivot = 'middle', 
           scale=3, linewidth = 0.2, units = 'xy', headwidth = 1)    # Uses matplotlib's quiver() to create a vector field without arrowheads
plt.axhline(0, c='black')       # Creates axis
plt.axvline(0, c='black')
plt.xlabel('x')
plt.ylabel('y')
plt.show()