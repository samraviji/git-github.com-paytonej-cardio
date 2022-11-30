"""
Created on Wed Nov 16 14:01:11 2022
VEC calculation
@author: kumarr6
"""

from mendeleev import element
import pandas as pd
df = pd.read_excel(r'\\clusterfsnew.ceas1.uc.edu\students\kumarr6\desktop\Research\VEC TC HC.xlsx')
print(df)




'''
Valence electron concentration
'''
import numpy as np
def vec(composition, comp_at_fract):
    
    x = []
    for index in np.arange(0,np.size(composition)):
        x.append(element(composition[index]).nvalence())
    
    xbar = np.dot(comp_at_fract, x)
    return xbar

# table Type A HEA from paper High Entropy alloy superconductors status, opportunities and challanges
"""
composition = ['Ta', 'Nb', 'Zr', 'Hf', 'Ti']
comp_fract = [0.35, 0.35, 0.1, 0.1, 0.1]
HEA_VEC: 4.700000000000001
"""
"""composition = ['Ta', 'Nb', 'Zr', 'Hf', 'Ti']
comp_fract = [0.35, 0.35, 0.11, 0.11, 0.11]
HEA_VEC: 4.679611650485436
"""

# composition = ['Ta', 'Nb', 'Zr', 'Hf', 'Ti']
# comp_fract = [34, 33, 14, 8, 11]
# HEA_VEC: 4.67

# composition = ['Ta', 'Nb', 'Zr', 'Hf', 'Ti']
# comp_fract = [0.35, 0.35, 0.13333333, 0.13333333, 0.13333333]
# HEA_VEC: 4.63636364214876

# composition = ['Ta', 'Nb', 'Zr', 'Hf', 'Ti']
# comp_fract = [0.35, 0.35, 0.16666666, 0.16666666, 0.16666666]
# HEA_VEC: 4.583333343055556

# composition = ['Ta', 'Nb', 'Zr', 'Hf', 'Ti']
# comp_fract = [0.35, 0.35, 0.28, 0.28, 0.28]
# HEA_VEC: 4.454545454545454

# composition = ['Ta', 'Nb', 'Hf']
# comp_fract = [33.5, 33.5, 33]
# HEA_VEC: 4.67

# composition = ['Ta', 'Nb', 'Zr', 'Hf']
# comp_fract = [33.5, 33.5, 16.5, 16.5]
# HEA_VEC: 4.67

# composition = ['Nb', 'Zr', 'Hf', 'Ti']
# comp_fract = [67, 11, 11, 11]
# HEA_VEC: 4.67

# composition = ['V', 'Nb', 'Zr', 'Hf', 'Ti']
# comp_fract = [33.5, 33.5, 11, 11, 11]
# HEA_VEC: 4.67

# composition = ['Ta', 'V', 'Zr', 'Hf', 'Ti']
# comp_fract = [33.5, 33.5, 11, 11, 11]
# HEA_VEC: 4.67

# composition = ['Ta', 'Nb', 'Zr', 'Hf', 'Ti']
# comp_fract = [33.5, 33.5, 11, 11, 11]
# HEA_VEC: 4.67

# composition = ['Ta', 'Nb', 'V', 'Zr', 'Hf', 'Ti']
# comp_fract = [22.3333333333333, 22.33333333333333, 22.33333333333333, 11, 11, 11]
# HEA_VEC: 4.67

# composition = ['Ta', 'Nb', 'Zr', 'Ti']
# comp_fract = [30.7, 25.2, 22.8, 21.3]
# HEA_VEC: 4.559

# composition = ['Ta', 'Nb', 'Zr', 'Hf', 'Ti']
# comp_fract = [26.3, 22.1, 15.5, 19.5, 16.6]
# HEA_VEC: 4.484

# composition = ['Ta', 'V', 'Zr', 'Hf', 'Ti','Nb']
# comp_fract = [18.1, 13.5, 14.4, 16.6, 15.9, 21.5]
# HEA_VEC: 4.531000000000001

# composition = ['Ta', 'Nb', 'Zr', 'Fe', 'Ti']
# comp_fract = [1, 1, 1, 1, 1]
# HEA_VEC: 5.2

# composition = ['Ta', 'Nb', 'Zr', 'Ge', 'Ti']
# comp_fract = [1, 1, 1, 1, 1]
# HEA_VEC: 4.4

# composition = ['Ta', 'Nb', 'Zr', 'Si', 'V', 'Ti']
# comp_fract = [1, 1, 1, 1, 1, 1]
# HEA_VEC: 4.5

# composition = ['Ta', 'Nb', 'Zr', 'Si', 'Ge', 'Ti']
# comp_fract = [1, 1, 1, 1, 1, 1]
# HEA_VEC: 4.333333333333333

# table Type B and mix HEA from paper High Entropy alloy superconductors status, opportunities and challanges

# composition = ['Zr', 'Nb', 'Mo', 'Re', 'Ru']
# comp_fract = [0.1, 0.1, 0.266666666666, 0.266666666666, 0.266666666666]
# (ZrNb)0.2(MoReRu)0.8HEA_VEC: 6.499999999998999

# composition = ['Zr', 'Nb', 'Mo', 'Re', 'Ru']
# comp_fract = [0.05, 0.05, 0.3, 0.3, 0.3]
# (ZrNb)0.1(MoReRu)0.9HEA_VEC: 6.75

# composition = ['Hf', 'Ta', 'W', 'Ir', 'Re']
# comp_fract = [0.15, 0.15, 0.15, 0.15, 0.4]
# (HfTaWIr)0.6Re0.4HEA_VEC: 6.4

# composition = ['Hf', 'Ta', 'W', 'Ir', 'Re']
# comp_fract = [0.125, 0.125, 0.125, 0.125, 0.5]
# (HfTaWIr)0.5Re0.5HEA_VEC: 6.5

# composition = ['Hf', 'Ta', 'W', 'Ir', 'Re']
# comp_fract = [0.1, 0.1, 0.1, 0.1, 0.6]
# (HfTaWIr)0.4Re0.6HEA_VEC: 6.600000000000001

# composition = ['Hf', 'Ta', 'W', 'Ir', 'Re']
# comp_fract = [0.075, 0.075, 0.075, 0.075, 0.7]
#(HfTaWIr)0.3Re0.7 HEA_VEC: 6.699999999999999

# composition = ['Hf', 'Ta', 'W', 'Ir', 'Re']
# comp_fract = [0.05, 0.05, 0.05, 0.05, 0.8]
# (HfTaWIr)0.2Re0.8HEA_VEC: 6.800000000000001

# composition = ['Hf', 'Ta', 'W', 'Pt', 'Re']
# comp_fract = [0.125, 0.125, 0.125, 0.125, 0.5]
# (HfTaWPt)0.5Re0.5HEA_VEC: 6.625

# composition = ['Hf', 'Ta', 'W', 'Pt', 'Re']
# comp_fract = [0.1, 0.1, 0.1, 0.1, 0.6]
# (HfTaWPt)0.4Re0.6HEA_VEC: 6.700000000000001

# composition = ['Hf', 'Ta', 'W', 'Pt', 'Re']
# comp_fract = [0.075, 0.075, 0.075, 0.075, 0.7]
# (HfTaWPt)0.3Re0.7HEA_VEC: 6.7749999999999995

# composition = ['Hf', 'Ta', 'W', 'Pt', 'Re']
# comp_fract = [0.05, 0.05, 0.05, 0.05, 0.75]
# (HfTaWPt)0.2Re0.75HEA_VEC: 6.842105263157895

# table Type C HEA from paper High Entropy alloy superconductors status, opportunities and challanges

# composition = ['Sc', 'Zr', 'Nb', 'Ta', 'Rh', 'Pd']
# comp_fract = [0.1625, 0.1625, 0.1625, 0.1625, 0.175, 0.175]
# (ScZrNbTa)0.65(RhPd)0.35HEA_VEC: 6.4375

# composition = ['Sc', 'Zr', 'Nb', 'Rh', 'Pd']
# comp_fract = [0.21, 0.21, 0.21, 0.185, 0.185]
# (ScZrNb)0.63(RhPd)0.37HEA_VEC: 6.404999999999999


# composition = ['Sc', 'Zr', 'Nb', 'Rh', 'Pd']
# comp_fract = [0.2066666666, 0.2066666666, 0.2066666666, 0.19, 0.19]
# (ScZrNb)0.62(RhPd)0.38HEA_VEC: 6.470000000494

# composition = ['Sc', 'Zr', 'Nb', 'Rh', 'Pd']
# comp_fract = [0.20, 0.20, 0.20, 0.20, 0.20]
# (ScZrNb)0.60(RhPd)0.40HEA_VEC: 6.6

# table Type D HEA from paper High Entropy alloy superconductors status, opportunities and challanges

# composition = ['Re', 'Nb', 'Ti', 'Zr', 'Hf']
# comp_fract = [0.56, 0.11, 0.11, 0.11, 0.11]
# Re0.56Nb0.11Ti0.11Zr0.11Hf0.11HEA_VEC: 5.790000000000001
comp_at_fract = comp_fract / np.sum(comp_fract)
my_vec = vec(composition, comp_at_fract)

print("HEA_VEC:",my_vec)