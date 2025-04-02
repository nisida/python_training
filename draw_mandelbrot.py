#!/usr/bin/env python
# # -*- coding:utf-8 -*-

"""
Draw Mandelbrot

 ref #1 --> https://www.dendoron.com/boards/25
     #2 --> https://watlab-blog.com/2020/05/23/mandelbrot-set/#i-3
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

print(__doc__)

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

class Mandelbrot:
    
    """Calc. Mandelbrot Set
    
    |Zn| > 2 -> 発散 (?)
    
    """
    def __init__(self, M, maxItr):
        self.M = M
        self.maxItr = maxItr

    def Calc(self, re, im): # re, im: 2d Array 
        """ Calc. Mandelbrot Set
        Args:
            re (float): real part of complex number Z
            im (float): image part of complex number Z

        Returns:
            Mandelbrot Value: complex number
        """
        x = 0.0
        y = 0.0

        for i in range(self.maxItr):
            
            if x**2 + y*2 > self.M:
                return i
            x_ = x**2 - y**2 + re
            y_ = 2*x*y + im
            x, y = x_, y_
        return self.maxItr
    
    def test(self) :
        
        """mandelbrot calc. test
        python complex number : https://note.nkmk.me/python-complex/
        """
        z0 = complex(0, 0)
        #c  = complex(0.1, 0.1)
        #c   = complex(-1, 0.5)
        c   = complex(0.2, 0.2)
        
        n = 0
        while np.abs(z0) < np.inf and not n == self.M:
            z0 = z0 ** 2 + c
            n += 1
            #print(z0)
 
        if n == self.M :
            msg = "c = {} + {}*j Convergence".format(c.real, c.imag)
        else :
            msg = "c = {} + {}*j Divvergence".format(c.real, c.imag)

        print(msg)

    def draw(self) :
        
        """ draw mandelbrot set
        """
        
        
        #self.M = 10000000
        #maxItr = 255
        #Mand = Mandelbrot(M, maxItr)

        x_lower = -2.5
        x_upper = 1.1
        y_lower = -1.8
        y_upper = 1.8
        pixel = 1000
        z = [[0 for m in range(pixel+1)] for n in range(pixel+1)]
        for i in range(pixel+1):
            re = x_lower + (x_upper - x_lower)/pixel * i 
            for j in range(pixel+1):
                im = y_lower + (y_upper - y_lower)/pixel * j
                z[j][i] = self.Calc(re, im)
    
        x = np.arange(pixel+1)
        y = np.arange(pixel+1)
        Z = np.array(z)
        X, Y = np.meshgrid(x, y)

        #print("X, Y, Z shape     = {}, {}, {}".format(X.shape, Y.shape, Z.shape))
        #print("X[1], Y[1] , Z[1] = {}, {}, {} ".format(X[1], Y[1], Z[1]))
        #print("X[2], Y[2] , Z[2] = {}, {}, {} ".format(X[2], Y[2], Z[2]))

        plt.rcParams['figure.figsize'] = 5, 5
        plt.gca().set_aspect('equal', adjustable='box')
        plt.pcolor(X, Y, Z)
        plt.colorbar()
        plt.hot()
        plt.xlabel('Re', fontsize=10)
        plt.ylabel('Im', fontsize=10)
        plt.xticks(color="None")
        plt.yticks(color="None")
        plt.tick_params(length=0)
        plt.show()

if __name__ == '__main__':
    
    obj = Mandelbrot(M = 10000000, maxItr = 255)
    #obj.draw()
    obj.test()



