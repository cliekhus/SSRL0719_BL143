# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 11:55:15 2019

@author: chels
"""

def averageScans(BaseName, NumRuns, ploton):
    
    from loadFile import loadFile
    import matplotlib.pyplot as plt
    
    ii = 0
    
    for runnum in range(NumRuns):

        print('Data/'+BaseName+'_'+'{0:03d}'.format(runnum+1)+'.dat')
        
        xenergy, i0, ff1, ff2, ff3, ff4 = loadFile('Data/'+BaseName+'_'+'{0:03d}'.format(runnum+1)+'.dat')
        
        if ii == 0:
            XEnergy = xenergy
            I0 = i0
            FF1 = ff1
            FF2 = ff2
            FF3 = ff3
            FF4 = ff4
        else:
            
            XEnergy = [x+y for x,y in zip(XEnergy,xenergy)]
            I0 = [x+y for x,y in zip(I0,i0)]
            FF1 = [x+y for x,y in zip(FF1,ff1)]
            FF2 = [x+y for x,y in zip(FF2,ff2)]
            FF3 = [x+y for x,y in zip(FF3,ff3)]
            FF4 = [x+y for x,y in zip(FF4,ff4)]
        
        if ploton:
            plt.plot(xenergy, [(x+y)/z for x,y,z in zip(ff1,ff2,i0)])
            plt.xlabel('xray energy (eV)')
            plt.title('XAS (TFY)')
            
    return XEnergy, I0, FF1, FF2, FF3, FF4