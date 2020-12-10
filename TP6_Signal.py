#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 09:35:19 2020

@author: elvinagovendasamy
"""
import numpy as np
from scipy.linalg import dft



# =============================================================================
# Exercice 1
# =============================================================================

# On obtient la convolution dans Z/nZ
# Part b)

f = np.array([0,1,2,3,4,5,6,7,8,9])
g = np.array([0,0,1,1,0,0,3,0,0,0])
# Transform en frequentiel par fourier.
a=np.fft.fft(f)
b=np.fft.fft(g)
# on fait le produit dans le domaine frequentiel
product=a*b
# On fait transformée de fourier inverse. # A VALIDER CA DOIT QUOI EXACTEMENT
result=np.fft.ifft(product).real




# =============================================================================
# Exercice 2
# =============================================================================
# Part a)
# On a -1000, -950,....950, 1000
# La fréquence commune minimum = 50
# Le nombre d'échantillon,N = 20 + 20 + 1 = 41
# e = la fréquence d'echantillonage = Nf = 41*50 = 2050

# Part b)
def MatriceFourrier(d):
    M = dft(d, scale = 'n')     #matrice de Fourier du cours
    M_inv = np.conj(d*M)
    return(M,M_inv)

