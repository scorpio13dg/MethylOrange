#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 11 16:57:12 2024

@author: niallgushue
"""

import numpy as np
import matplotlib.pyplot as plt


def Spec_Work_Function(KE,Counts):
    
    hv = 1253.6
    Lit_Gold_4f_72_BE = 83.8
    Max_Signal_Gold_4f = max(Counts)

    for i in range(len(Counts)):
        if Counts[i] == Max_Signal_Gold_4f:
            Max_Index = i
            
    KE = KE[Max_Index]

    BE = hv - KE

    Spectrometer_Work_Function_Gold = BE - Lit_Gold_4f_72_BE
    
    print(BE)
    return Spectrometer_Work_Function_Gold

hv = 1253.6
#==============================================================================
#For Pass Energy of 10eV

Gold_4f_Ep10 = np.loadtxt('Gold 4f Ep 10.txt')
Gold_4f_KE_Ep10 = Gold_4f_Ep10 [:,0] #First Column
Gold_4f_Counts_Ep10 = Gold_4f_Ep10 [:,1] #Second Colum

Gold_4f_BE_Ep10 = hv - Gold_4f_KE_Ep10


plt.plot(Gold_4f_BE_Ep10,Gold_4f_Counts_Ep10, 'ro', label = 'Au 4f Pass Energy: 10')
plt.xlabel('Binding Energy (eV)')
plt.ylabel('Counts/s')
plt.title('Gold 4f Spectrum')


Gold_4f_Ep10_Peak = np.loadtxt('Gold 4f 72 Peak Fit Ep 10.txt')
Gold_4f_KE_Ep10_Peak = Gold_4f_Ep10_Peak [:,0] #First Column
Gold_4f_Counts_Ep10_Peak = Gold_4f_Ep10_Peak [:,1] #Second Colum

Gold_4f_BE_Ep10_Peak = hv - Gold_4f_KE_Ep10_Peak

plt.plot(Gold_4f_BE_Ep10_Peak,Gold_4f_Counts_Ep10_Peak, 'blue', label = 'Au 4f Peak Fitting')
plt.xlabel('Binding Energy (eV)')
plt.ylabel('Counts/s')
plt.title('Gold 4f with Peak Fitting: Voigt Peak Function, Tougard Background')
plt.legend()
plt.xlim(100,80)
plt.show()

Pass_Energy_10_Work_Function = Spec_Work_Function(Gold_4f_KE_Ep10_Peak, Gold_4f_Counts_Ep10_Peak)

print(Pass_Energy_10_Work_Function)

#==============================================================================
#For Pass Energy of 50eV

Gold_4f_Ep50 = np.loadtxt('Gold 4f Ep 50.txt')
Gold_4f_KE_Ep50 = Gold_4f_Ep50 [:,0] #First Column
Gold_4f_Counts_Ep50 = Gold_4f_Ep50 [:,1] #Second Colum

Gold_4f_BE_Ep50 = hv - Gold_4f_KE_Ep50


plt.plot(Gold_4f_BE_Ep50,Gold_4f_Counts_Ep50, 'red', label = 'Au 4f Pass Energy: 50')
plt.xlabel('Binding Energy (eV)')
plt.ylabel('Counts/s')
plt.title('Gold 4f Spectrum')


Gold_4f_Ep50_Peak = np.loadtxt('Gold 4f 72 Peak Fit Ep 50.txt')
Gold_4f_KE_Ep50_Peak = Gold_4f_Ep50_Peak [:,0] #First Column
Gold_4f_Counts_Ep50_Peak = Gold_4f_Ep50_Peak [:,1] #Second Colum

Gold_4f_BE_Ep50_Peak = hv - Gold_4f_KE_Ep50_Peak

plt.plot(Gold_4f_BE_Ep50_Peak,Gold_4f_Counts_Ep50_Peak, 'blue', label = 'Au 4f Peak Fitting')
plt.xlabel('Binding Energy (eV)')
plt.ylabel('Counts/s')
plt.title('Gold 4f with Peak Fitting: Voigt Peak Function, Tougard Background')
plt.legend()
plt.xlim(80,100)

plt.show()


Pass_Energy_50_Work_Function = Spec_Work_Function(Gold_4f_KE_Ep50_Peak, Gold_4f_Counts_Ep50_Peak)

print(Pass_Energy_50_Work_Function)








