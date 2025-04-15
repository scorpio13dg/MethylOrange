#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  8 22:47:26 2024

@author: niallgushue
"""

 
import numpy as np
import matplotlib.pyplot as plt
from numpy.linalg import lstsq

# Source = input('What source was used? Al or Mg?')

# hv = 0

# if Source == 'Al':
#     hv = 1486.7 #ev

# elif Source == 'Mg':
#     hv = 1253.6 #ev
    

#Voight, Shirley, Asymetric Peak Fit was Best


hv = 1253.6 #Mg Source
    
#==============================================================================
#For Gold Calibration:

Lit_Gold_4f_72_BE = 83.8 #KeV , Binding Energy of the 4f 7/2

Gold_4f_File = np.loadtxt('Gold 4f copy.txt')
Gold_4f_KE = Gold_4f_File [:,0] #First Column
Gold_4f_Counts = Gold_4f_File [:,1] #Second Colum

plt.plot(Gold_4f_KE,Gold_4f_Counts)
plt.xlabel('Kinetic Energy (KeV)')
plt.ylabel('Counts/s')
plt.title('Gold 4f Spectrum')
plt.show()

Max_Signal_Gold_4f = max(Gold_4f_Counts)

for i in range(len(Gold_4f_Counts)):
    if Gold_4f_Counts[i] == Max_Signal_Gold_4f:
        Max_Index = i
        
Gold_4f_72_KE = Gold_4f_KE[Max_Index]

Measured_Gold_4f_72_BE = hv - Gold_4f_72_KE

Spectrometer_Work_Function_Gold = Measured_Gold_4f_72_BE - Lit_Gold_4f_72_BE

print(Spectrometer_Work_Function_Gold)

#==============================================================================
# #For Silver Calibration

# Lit_Ag_3d_52_BE = 368.3 #KeV , Binding Energy of the 3d 5/2

# Ag_3d_File = np.loadtxt('Gold 4f copy.txt')
# Ag_3d_KE = Ag_3d_File [:,0] #First Column
# Ag_3d_Counts = Ag_3d_File [:,1] #Second Colum

# plt.plot(Ag_3d_KE,Ag_3d_Counts)
# plt.xlabel('Kinetic Energy (KeV)')
# plt.ylabel('Counts/s')
# plt.title('Silver 3d Spectrum')
# plt.show()

# Max_Signal_Ag_3d = max(Ag_3d_Counts)

# for i in range(len(Ag_3d_Counts)):
#     if Ag_3d_Counts[i] == Max_Signal_Ag_3d:
#         Max_Index = i
        
# Ag_3d_52_KE = Ag_3d_KE[Max_Index]

# Measured_Ag_3d_52_BE = hv - Ag_3d_52_KE

# Spectrometer_Work_Function_Ag = Measured_Ag_3d_52_BE - Lit_Ag_3d_52_BE

# print(Spectrometer_Work_Function_Ag)
#==============================================================================

'''
P90 Band Gap Fit
'''

P90BG = np.loadtxt('P90 Band Gap copy.txt')
P90BG_KE = P90BG [:,0] #First Column
P90BG_Counts = P90BG [:,1] #Second Column

P90BG_BE = hv - P90BG_KE - Spectrometer_Work_Function_Gold
    
plt.plot(P90BG_BE, P90BG_Counts,'green', label = 'P90 Valence Band')
plt.xlabel('Binding Energy (eV)')
plt.ylabel('Counts/s')
plt.title('P90 Valence Band')


Fermi = np.loadtxt('Fermi Edge Fit copy.txt')
Fermi_KE = Fermi [:,0] #First Column
Fermi_Counts = Fermi [:,1] #Second Column

Fermi_BE = hv - Fermi_KE - Spectrometer_Work_Function_Gold

plt.plot(Fermi_BE, Fermi_Counts, 'blue', label = 'Fermi Edge Fit')
plt.xlim([15, -6])
plt.legend()
plt.show()


# plt.plot(Fermi_BE, Fermi_Counts)
# plt.xlabel('Binding Energy (eV)')
# plt.ylabel('Counts/s')
# plt.title('Fermi Edge Split')
# plt.show()



#==============================================================================
#Derivative Method

x = Fermi_BE
y = Fermi_Counts - 298

#xp = x[:-1]
#xpp = x[:-2]

yp = np.diff(y)/np.diff(x) #y prime
xp = (np.array(x)[:-1] + np.array(x)[1:]) / 2 #x prime

ypp = np.diff(yp)/np.diff(xp) #y double prime
xpp = (np.array(xp)[:-1] + np.array(xp)[1:]) / 2 #x double prime









plt.plot(x,y,'blue', label = 'P90 Raw Data Fit')
plt.plot(xp,yp,'red', label = 'P90 First Derivative')
plt.plot(xpp,ypp, 'green', label = 'P90 Second Derivative')
idx = np.argwhere(np.diff(np.sign(y[:554] - ypp))).flatten()
# plt.plot(x[idx], y[idx], 'ro')
plt.plot(xpp[231],ypp[231], 'ro')

# print(idx)
plt.xlim(0,5)
plt.ylim(-30,50)


plt.xlabel('Binding Energy (eV)')
plt.ylabel('Counts/s')
plt.title('Second Derivative Method: Valence Band = 2.3 eV')

plt.legend()


plt.show()


#==============================================================================
dy_test = y[1:]-y[:-1]
plt.scatter(x, y)
#plt.plot(dy_test)
plt.ylim([25, 30])
plt.xlim([3.75,4.1])
plt.show()


#==============================================================================
#Intercept Method


plt.plot(Fermi_BE, Fermi_Counts - 290)
plt.xlabel('Binding Energy (eV)')
plt.ylabel('Counts/s')
plt.title('Intercept Method: Valence Band = 2.6 eV')


plt.plot(Fermi_BE[120],Fermi_Counts[120] - 290, 'ro')
plt.plot(Fermi_BE[160],Fermi_Counts[160] - 290, 'ro')

points = [(Fermi_BE[120],Fermi_Counts[120] - 290),(Fermi_BE[160],Fermi_Counts[160] - 290)]
x_coords, y_coords = zip(*points)
A = np.vstack([x_coords,np.ones(len(x_coords))]).T
m, c = lstsq(A, y_coords)[0]
print("Line Solution is y = {m}x + {c}".format(m=m,c=c))

x = np.linspace(2.6, 4, 100)
y = 25.82 * x - 65.99
plt.plot(x, y)

plt.show()















