#!/usr/bin/env python
#coding=utf-8

"""
soving a quadratic equation
"""

from __future__ import division
import math

def quadratic_euation(a,b,c):
    delta = b*b - 4*a*c
    if delta < 0:
        return False
    elif delta == 0:
        return -(b/2*a)
    else:
        sqrt_delta = math.sqrt(delta)
        x1 = (-b + sqrt_delta)/2*a
        x2 = (-b - sqrt_delta)/2*a
        return x1,x2
        
if __name_ =="__main__":
    print "a quadratic equation:x^2 +2x +1 = 0"
    coefficients =(1,2,1) 
    roots =  quadratic_euation(*coefficients)
    if roots:
        print "the results is:",roots
    else:
    	  print "this equation has no solution."
