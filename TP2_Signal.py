#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 09:13:35 2020

@author: egovenda
"""
import math
import numpy as np
# =============================================================================
# Exercice 3 ++ avec le melange de 2 sons (simultanes) ++ gauche et droite
# =============================================================================

# transformation en bytes
def recadrage(m, M,v):# m=min et M=Max
    # volumezoome=(255/2)*(v+1) : on met 2 car c'est entre -1 et 1
    int_max_8ns=pow(2,8)-1 # comme on commence a 0 on n'a pas a faire le len
    int_max_16ns=pow(2,16)-1
    
    int_min_8s=(pow(2,8)/2)*-1
    int_max_8s=(pow(2,8)/2)-1
    
    int_min_16s=(pow(2,16)/2)*-1
    int_max_16s=(pow(2,16)/2)-1

    volumezoome_8ns=(int_max_8ns/(M-m))*(v-m)  
    volumezoome_16ns=(int_max_16ns/(M-m))*(v-m)   # pour le 16 bits non signes :A FAIRE LE 16 SIGNEES
    volumezoome_8s=((int_max_8s-int_min_8s)/(M-m))*(v-m) # 8 signed
    volumezoome_16s=((int_max_16s-int_min_16s)/(M-m))*(v-m) # 16 signed
    
    return int(volumezoome_8ns).to_bytes(1,byteorder='big',signed=False) # on convertit en bytes # MODIFIER SI 16 BITS






def signal1(t):
    return math.sin(2*np.pi*440*t) # on cree le signal
def signal2(t):
    return 0.5*math.sin(2*np.pi*660*t)
def signal(t):
    return signal1(t)+signal2(t)
    

delta=1/44100.
gauche=[]
droite=[]
tableau=[]
stereo=[]
signaux=[]
for steps in range(88200):
    temps=steps*delta #le temps varie entre 0 et 1 sec (si le range est de 0-44100), 0-88200 si 0-2seconds
    sig=signal(temps)
    sig1=signal1(temps)
    sig2=signal2(temps)
    gauche.append(sig1)
    droite.append(sig2)
    signaux.append(sig)
min_sig=min(signaux)
max_sig=max(signaux)
m_g=min(gauche)
M_g=max(gauche)
M_d=max(droite)
m_d=min(droite)
for sig in signaux:
    tableau.append(recadrage(min_sig,max_sig,sig)) # déjà en bytes
for i in range(len(gauche)):
    stereo.append(recadrage(m_g,M_g,sig1))
    stereo.append(recadrage(m_d,M_d,sig2))
    
    
f=open("fichier_read3.pcm","wb")
f_stereo=open("fichier_read4.pcm","wb")

for items in tableau:
    f.write(items)
    # write 
f.close()

for item in stereo:
    f_stereo.write(bytearray(item))
f_stereo.close()


# =============================================================================
# Using wave library: part 1
# =============================================================================
import wave, struct, random
sampleRate = 44100.0 # hertz
duration = 2.0 # seconds
frequency = 440.0 # hertz
obj = wave.open('sound.wav','w')
obj.setnchannels(1) # mono
obj.setsampwidth(2)
obj.setframerate(sampleRate)
for i in range(99999):
   value = random.randint(-32767, 32767) # 16 bits signés
   data = struct.pack('>h', value)
   obj.writeframesraw( data )
obj.close()



# =============================================================================
# Using scipy.io.wavefile library: part2
# =============================================================================

from scipy.io.wavfile import write

data = np.random.uniform(-1,1,44100) # 44100 random samples between -1 and 1
scaled = np.int16(data/np.max(np.abs(data)) * 32767)
write('test.wav', 44100, scaled)

# A faire pour le DO, RE, MI, FA SOL LA SI, joins ensemble


# =============================================================================
""" TP 2 """
# =============================================================================
# =============================================================================
# Produire un fichier Sol.wave
# =============================================================================

# https://docs.scipy.org/doc/scipy/reference/generated/scipy.io.wavfile.write.html
"""MONO"""
from scipy.io.wavfile import write
import numpy as np
sample=44100*3 # Si 44100 : la frequence plus rapide
fs=440*(2.**(-2/12)) # 440 sine wave
temps = np.linspace(0.,3.,sample) # 44100 temps
signal_Sol=np.sin(2*np.pi*fs*temps)
amplitude=np.iinfo(np.int16).max 
# 16_bit: np.int16 avec little ou big endian choisi automatiquement par scipy
# si 8bit: on met np.uint8 for unsiqned
data=signal_Sol*amplitude
# data is in 1 D for MONO, 2D array for stereo
write('Sol2.wav', 44100, data) #echantillon # il faut garder le bon taux [se aui se passe dans 1 sec]


"""STEREO qui joue deux sons differents : 1 son apres l'autre"""

from scipy.io.wavfile import write
import numpy as np
sample=44100*3
fs=440 # 440 sine wave
temps = np.linspace(0.,3.,sample) # 44100 temps 
s_La=np.sin(2*np.pi*fs*temps)
s_Si=np.sin(2*np.pi*fs*temps*2**(2/12))
amplitude=np.iinfo(np.uint8).max # fonctionne comme le recadrage mais il faudra l'ajuster et le changer pour faire le bon recadrage
# 16_bit: np.int16 avec little ou big endian choisi automatiquement par scipy
# si 8bit: on met np.uint8 for unsiqned
data_La=[s_La*amplitude]
data_Si=[s_Si*amplitude]
data=np.array([data_La,data_Si])
# data is in 1 D for MONO, 2D array for stereo
write('La_Si.wav', 44100, data) #echantillon




"""STEREO qui joue deux sons differents : 2 sons en meme temps"""
"""16 bits non signées: calculé avec l'amplitude"""


def recadrage_for_scipy_16ns(m, M,v):# m=min et M=Max, Type=soit 8ns, 8s, 16ns, 16s
    int_max_16ns=pow(2,16)-1
    volumezoome_16ns=(int_max_16ns/(M-m))*(v-m)   # pour le 16 bits non signes
    return int(volumezoome_16ns)

from scipy.io.wavfile import write
import numpy as np

sample=44100*3
fs=440 # 440 sine wave
temps = np.linspace(0.,3.,sample) # 44100 temps 
s_La=np.sin(2*np.pi*fs*temps)
s_Si=np.sin(2*np.pi*fs*temps*2**(2/12))
signal=s_La+s_Si
amplitude=np.iinfo(np.int16).max
# 16_bit: np.int16 avec little ou big endian choisi automatiquement par scipy
# si 8bit: on met np.uint8 for unsiqned
m_La=min(s_La)
M_La=max(s_La)
m_Si=min(s_Si)
M_Si=max(s_Si)

#recadrage_La=recadrage_for_scipy(m_La,M_La,signal)
data_La=np.array(np.int16(s_La*amplitude))
data_Si=np.array(np.int16(s_Si*amplitude))
data_array=np.array([data_La,data_Si]).T # we need to transpose
print(type(data_array))

# data is in 1 D for MONO, 2D array for stereo
write('La_Si.wav', 44100, data_array) #echantillon



# À REFAIRE POUR 8 BITS NON SIGNÉES




""" RECADRAGE"""

#def recadrage_for_scipy_16s(m, M,signal):# m=min et M=Max, Type=soit 8ns, 8s, 16ns, 16s
#    # volumezoome=(255/2)*(v+1) : on met 2 car c'est entre -1 et 1
#    int_min_16s=(pow(2,16)/2)*-1
#    int_max_16s=(pow(2,16)/2)-1
#    a=(int_max_16s-int_min_16s)/(M-m)
#    b=(int_min_16s*M-m*int_max_16s)/(M-m)
##    volumezoome_16s=((int_max_16s-int_min_16s)/(M-m))*(v-m) # 16 signed
#    
#    signal_new=a*signal+b
#    return np.int16(signal_new)


def recadrage_for_scipy_8s(m, M,v):# m=min et M=Max, Type=soit 8ns, 8s, 16ns, 16s
    # volumezoome=(255/2)*(v+1) : on met 2 car c'est entre -1 et 1

    int_min_8s=(pow(2,8)/2)*-1
    int_max_8s=(pow(2,8)/2)-1
    
    a=(int_max_8s-int_min_8s)/(M-m)
    b=(M*int_min_8s-m*int_max_8s)/(M-m)
    volumezoome_8s=a*v+b # 8 signed
    
    return int(volumezoome_8s)

def recadrage_for_scipy_16s(m, M,v):# m=min et M=Max, Type=soit 8ns, 8s, 16ns, 16s
    # volumezoome=(255/2)*(v+1) : on met 2 car c'est entre -1 et 1

    int_min_16s=(pow(2,16)/2)*-1
    int_max_16s=(pow(2,16)/2)-1
    a=(int_max_16s-int_min_16s)/(M-m)
    b=(M*int_min_16s-m*int_max_16s)/(M-m)
    volumezoome_16s=a*v+b 
    
    return np.int16(volumezoome_16s)


def signal_La(t):
    return np.sin(2*np.pi*440.*t) # on cree le signal
def signal_Si(t):
    return 0.5*np.sin(2*np.pi*440.*t*2**(2/12))
def signal(t):
    return signal_La(t)+signal_Si(t)

m_La=min(s_La)
M_La=max(s_La)
m_Si=min(s_Si)
M_Si=max(s_Si)
temps = np.linspace(0.,3.,sample) # 44100 temps 
sigLa=signal_La(temps)
sigSi=signal_Si(temps)
data_La=[]
for sig_La in sigLa:
    data_La.append(recadrage_for_scipy_8s(m_La,M_La,sigLa)*sigLa)



"""16 bits signées: calculé avec l'amplitude"""

from scipy.io.wavfile import write
import numpy as np


sample=44100*3
fs=440 # 440 sine wave
temps = np.linspace(0.,3.,sample) # 44100 temps 

s_La=np.sin(2*np.pi*fs*temps)
s_Si=np.sin(2*np.pi*fs*temps*2**(2/12))

s_La_2foismoinsfort=0.5*s_La
s_Si_2foismoinsfort=0.5*s_Si

s_La_Si=s_La+s_Si
# FAIRE LE SIGNAL 2 FOIS MOINS FORT
s_La_Si_2xmoinsfort=s_La_2foismoinsfort+s_Si_2foismoinsfort

m_La=min(s_La)
M_La=max(s_La)
m_Si=min(s_Si)
M_Si=max(s_Si)
m_LaSi=min(s_La_Si)
M_LaSi=max(s_La_Si)

La=recadrage_for_scipy_16s(m_La,M_La,s_La)
Si=recadrage_for_scipy_16s(m_Si,M_Si,s_Si)
La_Si_mono_mixed=recadrage_for_scipy_16s(m_LaSi,M_LaSi,s_La_Si)

La_Si_mono_mixed_2moins_fort=recadrage_for_scipy_16s(m_LaSi,M_LaSi,s_La_Si_2xmoinsfort) # ATTENTION ON GARDE LE MIN DU SIGNAL ORIGINAL(PAS DIVISER EN 2)


La_Si_stereo=np.array([La,Si]).T # we need to transpose
write('La_Si_mono_mixed_16s.wav', 44100, La_Si_mono_mixed)


write('La_Si_mono_mixed_moins_fort_16s.wav', 44100, La_Si_mono_mixed_2moins_fort)


write('La_Si_stereo_mixed_16s.wav', 44100, La_Si_stereo)


"""MONO qui joue deux sons differents : chaque son à part"""
""" VALIDER: quand/si on utilise gauche et droite pour jouer en MONO"""
""" VALIDER: On descend de 22 octave pour jouer 2 fois moins fort"""







# SON CONSTANT APRES A
from scipy.io.wavfile import write
import numpy as np


sample=44100*3
fs=440 # 440 sine wave
temps = np.linspace(0.,3.,sample) # 44100 temps 

s_La=[]
s_Si=[]
for t in temps:
    if 0<=t<=1:
        s_La.append(np.sin(2*np.pi*fs*t)*t)
        s_Si.append(np.sin(2*np.pi*fs*t*2**(2/12))*t)
    else:
        s_La.append(np.sin(2*np.pi*fs*t)*1)
        s_Si.append(np.sin(2*np.pi*fs*t*2**(2/12))*1)


s_La=np.array(s_La)
s_Si=np.array(s_Si)

s_La_Si=s_La+s_Si

m_La=min(s_La)
M_La=max(s_La)
m_Si=min(s_Si)
M_Si=max(s_Si)
m_LaSi=min(s_La_Si)
M_LaSi=max(s_La_Si)

La=recadrage_for_scipy_16s(m_La,M_La,s_La)
Si=recadrage_for_scipy_16s(m_Si,M_Si,s_Si)
La_Si_mono_mixed_constant=recadrage_for_scipy_16s(m_LaSi,M_LaSi,s_La_Si)



write('La_Si_mono_mixed_16s_sonconstantaprest=1.wav', 44100, La_Si_mono_mixed_constant)



# READING WAV FILE, GIVES OUT SAMPLE AND LENGTH OF SOUND(time)
from scipy.io.wavfile import read

fsample,data=read('La_Si_mono_mixed_16s.wav',mmap=False)
time=len(data)/fsample


# REDUCING 

fsample,data=read('La_Si_mono_mixed_16s.wav',mmap=False)
time=len(data)/fsample

temps = np.linspace(0.,time,sample) # 44100 temps 
s_La=[]
s_Si=[]
for t in temps:
    if 2<=t<=3:
        s_La.append(np.sin(2*np.pi*fs*t)*(3-t))
        s_Si.append(np.sin(2*np.pi*fs*t*2**(2/12))*(3-t))
    else:
        s_La.append(np.sin(2*np.pi*fs*t))
        s_Si.append(np.sin(-2*np.pi*fs*t*2**(2/12)))


s_La=np.array(s_La)
s_Si=np.array(s_Si)
s_La_Si=s_La+s_Si

m_La=min(s_La)
M_La=max(s_La)
m_Si=min(s_Si)
M_Si=max(s_Si)
m_LaSi=min(s_La_Si)
M_LaSi=max(s_La_Si)

La=recadrage_for_scipy_16s(m_La,M_La,s_La)
Si=recadrage_for_scipy_16s(m_Si,M_Si,s_Si)
La_Si_mono_baisserson=recadrage_for_scipy_16s(m_LaSi,M_LaSi,s_La_Si)


write('La_Si_mono_mixed_16s_sondiminueaprest=1.wav', 44100, La_Si_mono_mixed_baisserson)