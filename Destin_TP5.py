#!/usr/bin/env python3
# -*- coding: utf-8 -*-


#DA : TP5

# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 11:02:14 2020

@author: Destin Ashuza
"""

import numpy as np
import scipy.io.wavfile as siw
import matplotlib.pyplot as plt
from scipy.fft import fft

########################################## EXERCICE 1 ######################################

# question a

def question_a():
    f = np.arange(11) #f(x) = x pour x entier, 0 <= x <= 10 et f(x) = 0 sinon
    conv_f_f  = np.convolve(f, f) #convolution de f avec f 
    
    print(conv_f_f)
    

# question b
    
def question_b():
    """
    f(x) = x pour  -5 <= x <= 5 et f(x) = 0 sinon
    g(x) = x si x= 8,9 ou 10 et g(x) = 0 sinon
    f*g aura un décalage de -5+8=3 : il faut donc 
        ajouter [0,0,0] au début du résulat de 
        np.convolve correspondant à f*g de 0,1 et 2
    """
    
    f = np.arange(-5,6)
    g = np.arange(8,11)
    conv_f_g = np.convolve(f,g)
    
    #on ajoute ensuite le décalage :
    conv_f_g = np.append([0,0,0],conv_f_g)
    
    print(conv_f_g)
    

# question c
    
filename = "touche43.wav"

frequence_echantillonnage, t = siw.read(filename)
"""
frequence_echantillonnage
Out[23]: 44100

t
Out[24]: array([32767, 32207, 30502, ...,   528,   299,    21], dtype=int16)
"""

# question d

u = np.zeros(100001,dtype=np.float64)
for i in np.arange(start=20000,stop=100001,step=20000) :
    u[i] = (20000/i)**2
    
conv_t_u = np.convolve(t,u)

"""
conv_t_u.dtype
Out[45]: dtype('float64')
"""

# question e

def recadrage_float32(signal) :
    Max_depart = np.max(signal)
    Min_depart = np.min(signal)
    Max_arrivee = 1.0
    Min_arrivee = -1.0
    
    a = (Max_arrivee - Min_arrivee)/(Max_depart - Min_depart)
    b = (Max_depart*Min_arrivee - Max_arrivee*Min_depart)/(Max_depart - Min_depart)
    signal_recadre = a*signal+b
    return np.float32(signal_recadre)


w = recadrage_float32(conv_t_u)


# ou encore plus simple (seule différence : une seule borne sera atteinte : 1 ou -1 sauf si min = - max)

a = 1/max(abs(max(conv_t_u)),abs(min(conv_t_u)))
w_bis = np.float32(a*conv_t_u)

# question f

siw.write("touche43ech.wav",rate=44100,data=w)
siw.write("touche43ech_bis.wav",rate=44100,data=w_bis)

"""
Explication : dans u il y a juste 5 valeurs non nulles et qui sont décroissantes
     de 1 à 0.04. Ainsi, après recadrage, l'on joue le son initial suivi des 
     4 échos du même son d'amplitude de plus en plus faible
"""


########################################## EXERCICE 2 ######################################

# question a : fichier déjà téléchargé 

# question b :le tableau t a été produit à l'exercice 1 question c)

plt.plot(t)
plt.show()

# question c

"""
u = transformée de fourier de f sur les 21553 premières valeurs de t
(len(t)=21554 est pair mais on prend 21553 pour avoir un nombre de 
données impair nécessaire à la transformée de fourier)

t[:21553] est donc égal à t[:-1] ici

De plus on multiplie fft par 1/n = 1/21553 pour avoir les conventions du cours :
    M = 1/n*np.conj(M^-1)
La matrice M est celle qui doit être normalisée et M^-1 non, ce qui revient à :
    M = 1/n*fft
    M^-1 = n*ifft
    
Enfin les coefficients u sont obtenus dans l'ordre suivant :
    u = [c0, c1, ..., ck, c-k, ..., c-1]

La fonction fftshift peut donner les coefficients dans
l'ordre naturel si c'est ce que l'on veut :
    fftshift(u) = [c-k, ..., c-1, c0, c1, ..., ck]
    
Ici k = (21553-1)/2 = 10 776
"""

u = fft(t[:-1])/21553

# question d

"""
N = 21553 données (echantillons)
e = 44100 Hz (sample rate = fréquence d'échantillonnage)
f = e/N = 44100/21553 Hz ~= 2.046 Hz

frequences ordonnées = [-k*f, -(k-1)*f, ..., -f, 0, f, ..., (k-1)*f, k*f]

Le tableau des fréquences demandé :
    frequences = [0, f, ..., (k-1)*f, k*f, -k*f, -(k-1)*f, ..., -f]
"""

k = 10776
f = 44100/21553

frequences = f*np.append(np.arange(k+1),-np.arange(k,0,-1))

# question e

plt.plot(frequences, np.abs(u))
plt.show()

"""
La différence d'échelle pour l'axe des ordonnées constatée par rapport à la 
solution du prof est due à la normalisation faite en multipliant par 1/n
"""
##########################################################################

"""
autre solution pour un bon graphique (pour supprimer la ligne d'équation y = 0) : 
utiliser les tableaux "u" et "frequences" construits dans l'ordre naturel des 
coefficients de Fourier

la fonction np.fft.fftshift ou scipy.fftpack.fftshift reordonne 
les fréquences/coefficients suivant l'ordre naturel
"""
u_bis = np.fft.fftshift(u)
frequences_bis = np.fft.fftshift(frequences)

"""
On pourrait aussi construire directement le tableau dans le bon ordre par :
    frequences_bis = f*np.arange(-k,k+1)

Comme on n'a pas eu besoin de mettre les fréquences en leur vraie 
écriture complexe ici, on poourrait aussi juste les ordonner par :
    frequences_bis = np.sort(frequences)
et avoir le résultat voulu (ceci n'est pas possible avec les complexes)
"""

plt.plot(frequences_bis, np.abs(u_bis))
plt.show()

# question f

"""
Comme sur le graphique le premier pic se  trouve aux alentours de 320, il suffit
donc de trouver le max de la portion de |u_bis| correspondant à la  portion des 
fréquences du tableau frequences_bis comprises entre 200 Hz et 400 Hz par exemple
(voir l'intervalle autour du premier pic sur le graphique zoomé)
"""

#les indices des fréquences comprises entre 200Hz et 400Hz (dans le tableau ordonné) :
indices_200Hz_400Hz = np.where((200 <= frequences_bis) == (frequences_bis <= 400))
#indices_200Hz_400Hz est un tuple avec un seul élément qui est un array
#print(len(indices_200Hz_400Hz[0]))

#les fréqunces associées :
frequences_200Hz_400Hz = frequences_bis[indices_200Hz_400Hz]

#les coefficients associés :
u_200Hz_400Hz = u_bis[indices_200Hz_400Hz]

#les max
u_max_200Hz_400Hz = np.max(np.abs(u_200Hz_400Hz))

indice_du_max = np.where(np.abs(u_200Hz_400Hz) == u_max_200Hz_400Hz)

frequence_max = frequences_200Hz_400Hz[indice_du_max[0][0]]
"""
frequence_max
Out[192]: 321.2406625527769
"""



#######################################
# du prof:
# question c

"""
u = transformée de fourier de f sur les 21553 premières valeurs de t
(len(t)=21554 est pair mais on prend 21553 pour avoir un nombre de 
données impair nécessaire à la transformée de fourier)

t[:21553] est donc égal à t[:-1] ici

De plus on multiplie fft par 1/n = 1/21553 pour avoir les conventions du cours :
    M = 1/n*np.conj(M^-1)
La matrice M est celle qui doit être normalisée et M^-1 non, ce qui revient à :
    M = 1/n*fft
    M^-1 = n*ifft
    
Enfin les coefficients u sont obtenus dans l'ordre suivant :
    u = [c0, c1, ..., ck, c-k, ..., c-1]

La fonction fftshift peut donner les coefficients dans
l'ordre naturel si c'est ce que l'on veut :
    fftshift(u) = [c-k, ..., c-1, c0, c1, ..., ck]
    
Ici k = (21553-1)/2 = 10 776
"""

u = fft(t[:-1])/21553

# question d

"""
N = 21553 données (echantillons)
e = 44100 Hz (sample rate = fréquence d'échantillonnage)
f = e/N = 44100/21553 Hz ~= 2.046 Hz

frequences ordonnées = [-k*f, -(k-1)*f, ..., -f, 0, f, ..., (k-1)*f, k*f]

Le tableau des fréquences demandé :
    frequences = [0, f, ..., (k-1)*f, k*f, -k*f, -(k-1)*f, ..., -f]
"""

k = 10776
f = 44100/21553

frequences = f*np.append(np.arange(k+1),-np.arange(k,0,-1))







