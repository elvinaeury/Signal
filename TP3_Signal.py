#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 09:35:02 2020

@author: elvinagovendasamy
"""



# =============================================================================
""" Exo 1: Pour evaluer une fonction trigonometrie === en terme de exponentiel """
# =============================================================================
import numpy as np

c_liste=[1.,0.]
a_1=2
fs=200
temps=1/400


def evalPolyTrigo(t,f,c,a):
    f_ls=[]
    s=0
    for i in range(len(c)):
        f_ls.append((a+i)*f)
        s+=c[i]*np.exp(2*1j*np.pi*f_ls[i]*t)
    return s
        
result=evalPolyTrigo(temps,fs,c_liste,a_1)
    

        
# =============================================================================
""" Exo 2 : 
    # 1. Pour trouver les coeffs complexes, c 
    # 2. Pour trouver les coeffs a,b,c ... des cosinus et sinus """

# =============================================================================
a_ls=[1,2,0]
b_ls=[0,0,3]

def triToExp(a,b):
    c0=[a[0]]
    c_negatif=[]
    c_positif=[]
    for i in range(1,len(a)): # a et b ont la même longueur
        c_positif.append(0.5*(a[i]-b[i]*1j))
        # print(c_positif)
        c_negatif.append(0.5*(a[i]+b[i]*1j)) # ajoute c1, c2, c3 
        c_negatif=c_negatif[::-1]
        # print(c_negatif)
    return c0+c_positif+c_negatif

c_ls=triToExp(a_ls,b_ls)
print(c_ls) #c0,c1,c2,..c100,c-100,c-99,....c-1



def exptoTrig(c): # De dimension impair pour que c0 soit au milieu
    a=[c[0]] # il nous reste c_positif et c_negatif 
    b=[0] # car sin 0 = 0, peut importe la valeur de b, le résultat sera 0.
    c_positif=c[:((len(c)+1)//2)] # la premiere moitie
    
    for i in range(1,len(c_positif)): 
        a.append(2*c_positif[i].real) # on transforme en réelle car c'était complexe
        b.append(2*c_positif[i].imag)
    return [a,b]

result_a,result_b=exptoTrig(c_ls)        
        

# =============================================================================
""" Exo 3 : 
    # 1. Pour trouver la matrice M de fourier
    # 2. Pour trouver l'inverse de la matrice M """

# =============================================================================

from scipy.linalg import dft




# Fonction renvoyant matrice de Fourier et matrice inverse de Fourier
def matrice_fourier(degre):
    M=dft(degre,scale='n') # matrice Fourier (mtd du prof, n normalization)
    M_inv=np.conj(degre*M) #  matrice inverse de Fourier
    
    return (M,M_inv)



# Ou fonction pour calculer uniquement la matrice inverse
def matrice_inverse_fourier(degre,M):
    M_inv=np.conj(degre*M)
    return M_inv


d=3
matrice_M=matrice_fourier(d)[0]
matrice_M_inverse=matrice_fourier(d)[1] # c'est cette matrice qui a 1,1,1 sur la premiere ligne et premiere colonne

# =============================================================================
"""Exercice 4: Utiliser la transformee de Fourier  et matrice inverse pour trouver les valeurs de s"""
# =============================================================================
""" On obtient:
    s(t)= 1 + 2Cos(2pit) + 3Sin(8pit)
    
    f minimum commun = 2
    
    s(t)= 1xCos(0.2pi.2t) + 2xCos(1.2pi.2t) + 0xCos(2.2pi.2t) + 
          0xSin(0.2pi.2t) + 0xSin(1.2pi.2t) + 3xSin(3.2pi.2t)
    a=[1,2,0]
    b=[0,0,3]
        
    s(t)= c0 + c1.exp(2i.pi.2t) + c2.exp(2i.pi.8t) 
        + c-1.exp(-2i.pi.2t) + c-2.exp(-2i.pi.2t)
    C'est sur 5 dimensions. Pour aller sur 9 dimensions, on introduit 4 entrées au MILIEU:
      
    s(t)= c0 + c1.exp(2i.pi.2t) + c2.exp(2i.pi.8t) + [ c3.exp(2i.pi.4t) + c4.exp(2i.pi.6t) ]
        + c-1.exp(-2i.pi.2t) + c-2.exp(-2i.pi.2t) + [ c-3.exp(-2i.pi.4t) + c-4.exp(-2i.pi.6t) ]
        
    c3, c4, c-3, c-4 SERONT À 0
               
"""
  

"""
Pour trouver le signal s(t)
s(t)*M=(c0 c1 ... ct)
s(t)=M_inv*(c0 c1 .... ct)

"""
      
# Part c) # A VERIFIER JE N'OBTIENS PAS LE C0 DANS MA LISTE ON DIRAIT
M_inverse_exo4=matrice_fourier(9)[1]
# c0 = 1
# c1 = 1
# c2 = -1.5j
# c3 = 1.5j ....

c=[1,1,0,0,-3*1j/2,3*1j/2,0,0,1] # ATTENTION: l'ordre des c = c0, c1, ...,c4,c-4,...,c-1
# co,c1,c2,c3,c4,c-4,c-3,c-2,c-1 : On voit que c3,c4,c-3,c-4 sont mis à 0 

valeur_signal_exo4=np.dot(M_inverse_exo4,c).real


# =============================================================================
""" Exercice 5 """
# =============================================================================
"""         0           1           2                   3
    s(t) = 200 + 2xCos(500pit) + 10xCos(1000pit) + 3xSin(1500pit)

    f minimum commun est 250
    
    s(t)= 200xCos(0.2pi.250t) + 2xCos(1.2pi.250t) + 10xCos(2.2pi.250t) + 0xCos(3.pi.250t) +
          0xSin(0.2pi.250t) + 0xSin(1.2pi.250t) + 0xSin(2.2pi.250t) + 3xSin(3.2pi.250t)
          
    a = [200,2,10,0]
    b = [0,0,0,3] # ATTENTION SIN 0 = 0
    
    
"""
a_exo5 = [200,2,10,0]
b_exo5=[0,0,0,3]

c_exo5=triToExp(a_exo5,b_exo5)
# [200,(1+0j),(5+0j),-1.5j,1.5j,(1+0j),(5+0j)]

d_exo5=7 # Le nombre de c

M_inverse_exo5=matrice_fourier(d_exo5)[1]
valeur_signal_exo5=np.dot(M_inverse_exo5,c_exo5).real



""" Si on fait l'inverse on a les valeurs des signaux et on veut trouver les c """

# def signal_exponentiel(t):
#     return (200 + np.exp(-500*1j*np.pi*t) + np.exp(1000*1j*np.pi*t) + np.exp(1500*1j*np.pi*t) + np.exp(-1500*1j*np.pi*t)
#            +np.exp(-1000*1j*np.pi*t) + np.exp(-500*1j*np.pi*t))

def signal_trigo(t):
    return (200 + 2*np.cos(500*np.pi*t)+ 10*np.cos(1000*np.pi*t) + 3*np.sin(1500*np.pi*t))

# vecteur de valeurs de s

S1=[]
for i in range(0,d_exo5):
    S1.append(signal_trigo(i/(d*250)))

print(S1)
M_exo5=matrice_fourier(d_exo5)[0]
coeff_c=np.round(np.dot(M_exo5,S1),2) # vecteur contenant les coefficients c
# Avant j'ai obtenu : [200,(1+0j),(5+0j),-1.5j,1.5j,(1+0j),(5+0j)], avec ma fonction
# Ici on a  (201.71+0.0j), (1.86+0.89j), (3.6+4.52j), (-0.32-1.39j), (-0.32+1.39j), (3.6-4.52j), (1.86-0.89j)
""" A VALIDER JE NOBTIENS PAS VRAIMENT LA MEME CHOSE ENTRE MA FONCTION ET LA MATRICE """


    



