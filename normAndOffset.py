# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 16:49:59 2019

@author: chels
"""

def normAndOffset(I0, FF1, FF2, XEnergy, lowEnergy, highEnergy):
    
    import statistics as stat
    
    signal = [(x+y)/z for x,y,z in zip(FF1,FF2,I0)]
    offset = stat.mean([x for x,y in zip(signal, XEnergy) if y <= lowEnergy])
    
    signal = [x-offset for x in signal]
    
    norm = stat.mean([x for x,y in zip(signal, XEnergy) if y >= highEnergy])
    signal = [x/norm for x in signal]
    
    return signal


def normAndOffsetCl(I0, FF1, FF2, XEnergy, lowEnergyPre, lowEnergyPost, highEnergy):
    
    import statistics as stat
    
    signal = [(x+y)/z for x,y,z in zip(FF1,FF2,I0)]
    offset = stat.mean([x for x,y in zip(signal, XEnergy) if y <= lowEnergyPost and y >= lowEnergyPre])
    
    signal = [x-offset for x in signal]
    
    norm = stat.mean([x for x,y in zip(signal, XEnergy) if y >= highEnergy])
    signal = [x/norm for x in signal]
    
    return signal