# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import matplotlib.pyplot as plt
import numpy as np

# x = np.arange(0,100,0.1)
# y = np.sin(x)
# y2 = np.sin(x+0.2)**2.
# y3 = np.cos(x)/3.

# plt.figure()
# plt.plot(x, y, '--r')
# plt.plot(x, y2, '-b')
# plt.plot(x, y3, '*k')
# plt.xlabel('Angle, in radians')
# plt.ylabel('Function value')
# plt.show()



'''
Valence electron concentration
'''
def vec(composition, comp_at_fract):
    from mendeleev import element
    
    x = []
    for index in np.arange(0,np.size(composition)):
        x.append(element(composition[index]).nvalence())
    
    xbar = np.dot(comp_at_fract, x)
    return xbar

composition = ['Al', 'Ni', 'Cu', 'Co']
comp_fract = [1, 1, 1, 1]

comp_at_fract = comp_fract / np.sum(comp_fract)

my_vec = vec(composition, comp_at_fract)

print(my_vec)
"""
""VEC determination"

from mendeleev import Co,Al,Cu,Ni,Nb,Re,B,W
print("Co's electronic configuration: ", Co.econf)

print ("Co's valence electrn:", Co.nvalence())

print("Al's electronic configuration: ", Al.econf)

print ("Al's valence electrn:", Al.nvalence())

print("Cu's electronic configuration: ", Cu.econf)

print ("Cu's valence electrn:", Cu.nvalence())

print("Ni's electronic configuration: ", Ni.econf)

print ("Ni's valence electrn:", Ni.nvalence())

print("Nb's electronic configuration: ", Nb.econf)

print ("Nb's valence electrn:", Nb.nvalence())

print("Re's electronic configuration: ", Re.econf)

print ("Re's valence electrn:", Re.nvalence())

print("B's electronic configuration: ", B.econf)

print ("B's valence electrn:", B.nvalence())

print("W's electronic configuration: ", W.econf)

print ("W's valence electrn:", W.nvalence())
"""