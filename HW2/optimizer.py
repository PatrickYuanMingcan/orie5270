# -*- coding: utf-8 -*-
"""
Created on Thu Aug 23 21:35:26 2018

@author: yuan
"""

import numpy as np
from scipy.optimize import minimize

#Rosenbrock function, n = 3
def Rosenbrock(x):
    return 100*(x[1] - x[0]**2)**2 + (1 - x[0])**2 + 100*(x[2] - x[1]**2)**2 + (1 - x[1])**2

#gradient of Rosenbrock
def grad(x):
    return np.array([-400*x[1]*x[0] + 400*x[0]**3 + 2*x[0] - 2,
                     200*(x[1] - x[0]**2) - 400*x[2]*x[1] + 400*x[1]**3 + 2*x[1] - 2,
                     200*(x[2] - x[1]**2)])

if __name__ == "__main__":
    #create 10 starting points with N(0, 10)
    start_x = 10 * np.random.randn(10, 3)
    fun = []
    ret = []
    for x in start_x:
        fun.append(minimize(Rosenbrock, x, method = 'BFGS', jac = grad).fun)
        ret.append(minimize(Rosenbrock, x, method = 'BFGS', jac = grad).x)
    #print the minimize point with least fun
    print(ret[np.argmin(fun)])