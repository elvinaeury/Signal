#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 10:06:42 2020

@author: elvinagovendasamy
"""

import numpy as np
from numpy.fft import fft,ifft
import matplotlib.pyplot as plt
from math import pi
import pandas as pd
from scipy.linalg import dft


# Exercice 1 - 

# =============================================================================
# Question a
# =============================================================================


meteo1=pd.read_csv('meteo.csv',sep=';').loc[:,'Temperature']
temp=meteo1[0:25] # temp est une serie, on ne peut prend que les 25 premieres lignes
temp=temp.astype({'Temperature':float})

x = range(25)

plt.plot(x,temp)

# =============================================================================
# Question b)
# =============================================================================

#on a choisi N=25, et e= 1mesure/h donc f= 1.1e-5 Hz
#les fréquences complexes sont donc [-12f,...,-f,0,f,...,12f]
#on calcul les coefficients associés à ces fréquences


#Fonction renvoyant le matrice de fourier et la matrice inverse de fourier

def MatriceFourrier(d):
    M = dft(d, scale = 'n')     #matrice de Fourier du cours
    M_inv = np.conj(d*M)
    return(M,M_inv)
    
M = MatriceFourrier(25)[0]
M_inverse = MatriceFourrier(25)[1]

coefficients= np.dot(M,temp) #attention à l'ordre des coefs, le premier est c0 puis c1 jusqu'à c12 puis c-12 jusqu'à c-1



# =============================================================================
# Question c) A BIEN COMPRENDRE
# =============================================================================
# On veut la temperature à l'heure
# Les frequences sont toujours en secondes
# Alors on a 60*60 = 3600 secondes
# On a e=1/3600 = 2.78e-4
# Nf=e
#f=e/N =(1/3600)/25


f=(1/3600)/25
print(f)
liste_freq= np.array([k*f for k in range(13)]+[k*f for k in range(-12,0)])

def temperature(t,coeff):
    freq=2*np.pi*1j*3600*t*liste_freq
    vect_exp=np.exp(freq)
    valeurs=np.dot(coeff,vect_exp)
    signal_real=np.real(valeurs)
    return (signal_real)


# =============================================================================
# Question d)  A BIEN COMPRENDRE
# =============================================================================

time=np.linspace(0,25,100)

signal=[temperature(t,coefficients) for t in time]
values=[temperature(t_,coefficients) for t_ in x]




# for t in x:
#     values.append(temperature(t,coefficients))

    
plt.scatter(x,values,c='r',s=5)
plt.plot(time,signal,c='green')
    

# =============================================================================
# Question e)  A FAIRE
# =============================================================================



    
    
    
    
    
    