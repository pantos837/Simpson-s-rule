#!/usr/bin/env python
# coding: utf-8

# In[8]:


globals().clear()

import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as opt


# x_1 Lower limit of integration              
# x_2 Uper limit of integration
# n Number of divisions (always even)
# Eps Accuracy

# Define lower limit
x_1 =-1

# Define uper limit
x_2 =4

# Define number of subintervarls(must be even)
n =4

# Define the desired accuracy
Eps = 0.01

# Define fuction to integrate

def f(x):                 
    return np.cos(x)*x**2



def simpsons_rule(f,x_1,x_2,n):
     if n % 2 != 0:
        raise ValueError("Number of subintervals (n) must be even.")
     h = (x_2-x_1)/n                                     #Difference
     result = f(x_1) + f(x_2)
     matrix = np.empty(n+1,float)
     matrix[[0]] = x_1 
     matrix[[n]] = x_2 
        
     for i in range(1, n):
            matrix[[i]] = x_1 + i * h
            if i % 2 == 0:
                result += 2 * f(matrix[[i]])
                
            else:
                result += 4 * f(matrix[[i]])
# Plot the fuction graph and the aproxximation graph              
     x = np.linspace(x_1,x_2,1000)
     
     plt.rcParams["figure.autolayout"] = True
     plt.plot(x, f(x),color="red", label="Fuction Graph")
     plt.fill_between(x, f(x), step="pre", alpha=0.4)
     plt.plot(matrix,f(matrix),color="green",linestyle='dashed', linewidth = 2,
         marker='o', markerfacecolor='blue', markersize=6,label="Aproximation")
     leg = plt.legend(loc='lower left')
     # Display the graph
     plt.show()

     result *= h / 3 
     return result

# Error estimation
interval = (x_1, x_2)  # interval (start, end)

# Use the minimize_scalar function to find the maximum
result = opt.minimize_scalar(lambda x: -f(x), bounds=interval, method='bounded')
result_min = opt.minimize_scalar(f, bounds=interval, method='bounded')

if result.success:
    maximum_value = -result.fun  # Get the maximum value
    maximum_location = result.x  # Get the location of the maximum
    
    print(f"Maximum value: {maximum_value}")
    print(f"Location of maximum: {maximum_location}")

    minimum_value = result_min.fun  # Get the minimum value
    minimum_location = result_min.x  # Get the location of the minimum
    
    print(f"Minimum value: {minimum_value}")
    print(f"Location of minimum: {minimum_location}")
else:
    print("Optimization did not succeed.")

# We use a negative sign to find the maximum because `minimize_scalar` finds the minimum by default.

def Calculate_integral(f,x_1,x_2,n):
    integral = simpsons_rule(f,x_1,x_2,n)
    
    if Eps <= ((x_2 -x_1)**5/(180*n**4))*maximum_value:
        
        while Eps <= ((x_2 -x_1)**5/(180*n**4))*maximum_value:
            n +=2
            integral = simpsons_rule(f,x_1,x_2,n)
    
    if Eps >= ((x_2 -x_1)**5/(180*n**4))*maximum_value:
        
         print(f"The approximate value of integral is: {integral}") 
    
    
         return integral
    
  


result = Calculate_integral(f,x_1,x_2,n)        



# In[ ]:




