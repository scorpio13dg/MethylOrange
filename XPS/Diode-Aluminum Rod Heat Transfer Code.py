#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  6 21:12:31 2024

@author: niallgushue
"""

import numpy as np
import matplotlib.pyplot as plt
import timeit

# Constants
L = 0.063         # Thickness of aluminum in meters
D = 4.25e-6       # Thermal diffusivity
N = 100           # Number of divisions in grid
dx = L / N        # Grid spacing dx = 0.0001 m
dt = 5e-4         # Time-step: try different values, e.g., 3e-4
epsilon = dt / 100.

Tlo = 22           # Low temperature in Celsius
Tmid = 22         # Intermediate T in Celsius
Thi = 22        # High temperature in Celsius

times = [0, 5, 15, 60, 600]

# Create arrays for the temperature profile: T and T_new
T = np.ones(N + 1, float) * Tmid
T[0] = Thi  # Boundary condition at the bottom
T[-1] = Tlo  # Boundary condition at the top

# Diode parameters
Tdiode = 22 #Initial Temperature of the Diode
k_diode = 31.99  # Thermal conductivity of the diode in W/(m*K)
L_diode = 0.01  # Length of the diode in meters
P_diode =  2 * 2.59 * 0.2  # Power output of the diode in watts with two diodes and 20% is heat

# Set initial temperature for the diode region
diode_index = int(L_diode / dx)
T[1:diode_index + 1] = Tdiode

T_new = np.copy(T)

# Main loop
t = 0.0
coef = dt * D / dx ** 2

plt.plot(T, linewidth=2.0, label="t = %5.2f s" % (t))

start = timeit.default_timer()
while t < times[-1] + epsilon:
    # Calculate the new values of T
    T_new[1:N] = T[1:N] + coef * (T[2:N + 1] + T[0:N - 1] - 2 * T[1:N])
    
    # Apply boundary conditions for the diode
    T_new[1:diode_index + 1] += dt * P_diode / (k_diode * L_diode)
    
    # Ensure maximum temperature is 100 degrees Celsius
    T_new[T_new > 100] = 100
    
    # Make plots at given times
    for i in range(len(times)):
        if abs(t - times[i]) < dt / 2.:
            plt.plot(T, linewidth=2.0, label="t = %5.2f s" % (t))
    
    # Use T_new as the input for the next time step
    T = np.copy(T_new)
    
    t += dt

time = timeit.default_timer() - start
print("Total Computing Time:%7.2f seconds" % (time))

plt.xlabel("x", fontsize=14)
plt.ylabel("Temperature (°C)", fontsize=14)
plt.legend()
plt.show()