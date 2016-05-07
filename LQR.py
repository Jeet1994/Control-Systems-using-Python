Python 2.7.10 (default, May 23 2015, 09:44:00) [MSC v.1500 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import numpy as n
>>> from control import *
>>> A = n.matrix('0 1;0 0')
>>> B = n.matrix('0;1')
>>> Q = n.matrix('1 0;0 0')
>>> R = n.matrix('1')
>>> K,S,E = lqr(A,B,Q,R)
>>> K
array([[ 1.        ,  1.41421356]])
>>> S
array([[ 1.41421356,  1.        ],
       [ 1.        ,  1.41421356]])
>>> E
array([-0.70710677+0.70710677j, -0.70710677-0.70710677j], dtype=complex64)
>>> 
