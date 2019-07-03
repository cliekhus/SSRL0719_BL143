# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

"""
Real Time Clock
Requested Energy
I0   
I1   
I2   
I3   
MPFB1   
MPFB2   
FF1   
FF2   
FF3   
FF4   
ICR1   
ICR2   
ICR3   
ICR4   
SCA2.1   
SCA2.2   
SCA2.3   
SCA2.4   
TIME1   
TIME2   
TIME3  
"""

def loadFile(Filename):

    f = open(Filename)
    content = f.read()
    contentp = content.split('TIME4   \n\n')
    contentpp = contentp[1].split('\t')
    
    XEnergy = []
    I0 = []
    FF1 = []
    FF2 = []
    FF3 = []
    FF4 = []
    
    for ii in range(len(contentpp)):
        
        if ii%24 == 1:
            XEnergy = XEnergy + [float(contentpp[ii])]
        
        if ii%24 == 2:
            I0 = I0 + [float(contentpp[ii])]
            
        if ii%24 == 8:
            FF1 = FF1 + [float(contentpp[ii])]
            
        if ii%24 == 9:
            FF2 = FF2 + [float(contentpp[ii])]
            
        if ii%24 == 10:
            FF3 = FF3 + [float(contentpp[ii])]
            
        if ii%24 == 11:
            FF4 = FF4 + [float(contentpp[ii])]
            
    return XEnergy, I0, FF1, FF2, FF3, FF4
