#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 20 13:13:09 2024

@author: niallgushue
"""

import numpy as np
import matplotlib.pyplot as plt

WB_Weight = np.loadtxt('Weigh Bottle Mass.txt')
WB_Weights =  WB_Weight[:] #First Column

WBC_Weight = np.loadtxt('Weigh Bottle and Catalysts Mass.txt')
WBC_Weights =  WBC_Weight[:] #First Column


Diff_Weights = WBC_Weight - WB_Weight

Diff_Avg = np.average(Diff_Weights)
Diff_STD = np.std(Diff_Weights) * 1000
Diff_Avg_mg = Diff_Avg * 1000

print("The Catalyst Mass is",Diff_Avg_mg, "+/-", Diff_STD, 'mg')