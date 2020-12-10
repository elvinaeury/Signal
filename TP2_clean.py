#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 11 09:20:28 2020

@author: elvinagovendasamy
"""
import numpy as np
from scipy.io.wavfile import write
# =============================================================================
# Recadrage
# =============================================================================


#"""Destin version"""
#def recadrage_for_scipy_8s(m, M,v):# m=min_signal et M=Max_signal, Type=soit 8ns, 8s, 16ns, 16s
#    # volumezoome=(255/2)*(v+1) : on met 2 car c'est entre -1 et 1
#
#    int_min_8s=(pow(2,8)/2)*-1
#    int_max_8s=(pow(2,8)/2)-1
#    
#    a=(int_max_8s-int_min_8s)/(M-m)
#    b=(M*int_min_8s-m*int_max_8s)/(M-m)
#    volumezoome_8s=a*v+b # 8 signed
#    
#    return np.int8(volumezoome_8s)
#"""Other tests"""
#def recadrage_for_scipy_8ns(v):# m=min et M=Max, Type=soit 8ns, 8s, 16ns, 16s
#    # volumezoome=(255/2)*(v+1) : on met 2 car c'est entre -1 et 1
#
#    amplitude=np.iinfo(np.uint8).max 
#    
#    return np.uint8(amplitude*v)
#
#
#def recadrage_for_scipy_16s(m, M,v):# m=min et M=Max, Type=soit 8ns, 8s, 16ns, 16s
#    # volumezoome=(255/2)*(v+1) : on met 2 car c'est entre -1 et 1
#
#    int_min_16s=(pow(2,16)/2)*-1
#    int_max_16s=(pow(2,16)/2)-1
#    a=(int_max_16s-int_min_16s)/(M-m)
#    b=(M*int_min_16s-m*int_max_16s)/(M-m)
#    volumezoome_16s=a*v+b 
#    
#    return np.int16(volumezoome_16s)
#
#def recadrage_for_scipy_16ns(v):# m=min et M=Max, Type=soit 8ns, 8s, 16ns, 16s
#    # volumezoome=(255/2)*(v+1) : on met 2 car c'est entre -1 et 1
#
#    amplitude=np.iinfo(np.uint16).max
#    
#    return np.uint16(amplitude*v)
#

"""Elvi version"""
def recadrage_for_scipy_8s_elvi(ms, Ms,s):# ms=min_signal et Ms=Max_signal, s=signal
    # volumezoome=(255/2)*(v+1) : on met 2 car c'est entre -1 et 1

    min_8s=(pow(2,8)/2)*-1
    max_8s=(pow(2,8)/2)-1
    
    a=(max_8s-min_8s)/(Ms-ms)
    
    y_8s=a*(s-ms)+min_8s # 8 signed
    
    return np.int8(y_8s)

def recadrage_for_scipy_16s_elvi(ms, Ms,s):# ms=min_signal et Ms=Max_signal, s=signal
    # volumezoome=(255/2)*(v+1) : on met 2 car c'est entre -1 et 1

    min_16s=(pow(2,16)/2)*-1
    max_16s=(pow(2,16)/2)-1
    
    a=(max_16s-min_16s)/(Ms-ms)
    
    y_16s=a*(s-ms)+min_16s # 16 signed
    
    return np.int16(y_16s)


def recadrage_for_scipy_8ns_elvi(ms, Ms,s):# ms=min_signal et Ms=Max_signal, s=signal
    # volumezoome=(255/2)*(v+1) : on met 2 car c'est entre -1 et 1

    amplitude=np.iinfo(np.uint8).max #255
    
    a=amplitude/(Ms-ms)
    
    y_8ns=a*(s-ms) # 8 unsigned
    
    return np.uint8(y_8ns)


def recadrage_for_scipy_16ns_elvi(ms, Ms,s):# ms=min_signal et Ms=Max_signal, s=signal
    # volumezoome=(255/2)*(v+1) : on met 2 car c'est entre -1 et 1

    amplitude=np.iinfo(np.uint16).max 
    
    a=amplitude/(Ms-ms)
    
    y_16ns=a*(s-ms) # 16 unsigned
    
    return np.uint8(y_16ns)







# =============================================================================
# Signal
# =============================================================================

def signal_La(duration,rate):
    t=np.linspace(0,duration,duration*rate)
    return np.sin(2*np.pi*440.*t) # on cree le signal
def signal_Si(duration,rate):
    t=np.linspace(0,duration,duration*rate)
    return np.sin(2*np.pi*440.*t*2**(2/12)) # 2 fois moins fort = 0.5 *
def signal_Do(duration,rate):
    t=np.linspace(0,duration,duration*rate)
    return np.sin(2*np.pi*440.*t*2**(3/12))
def signal_Re(duration,rate):
    t=np.linspace(0,duration,duration*rate)
    return np.sin(2*np.pi*440.*t*2**(5/12))
def signal_Mi(duration,rate):
    t=np.linspace(0,duration,duration*rate)
    return np.sin(2*np.pi*440.*t*2**(7/12))
def signal_Fa(duration,rate):
    t=np.linspace(0,duration,duration*rate)
    return np.sin(2*np.pi*440.*t*2**(8/12))
def signal_Sol(duration,rate):
    t=np.linspace(0,duration,duration*rate)
    return np.sin(2*np.pi*440.*t*2**(10/12))
def signal_LaNextOctave(duration,rate):
    t=np.linspace(0,duration,duration*rate)
    return np.sin(2*np.pi*440.*t*2**(12/12))



# Mixing Signals
def signalLaSi(duration,rate):
    return signal_La(duration,rate)+signal_Si(duration,rate)

# =============================================================================
# Temps
# =============================================================================
# n= est en float exemple 3. pour 3 seconds
# sample: pour 3. seconds est 3*44100
# Attention: si on met sample sur 1*44100 et n sur 3 seconds, on augmente la fréquence
def temps_(n,sample):
    return(np.linspace(0.,np.float(n),sample))



# =============================================================================
# Application on 0.5 seconds: DoDoDoReMiDo
# =============================================================================


d,d1=0.5,1
r=44100



sigLa=signal_La(d,r)
sigSi=signal_Si(d,r)
sigDo=signal_Do(d,r)
sigRe=signal_Re(d,r)
sigMi=signal_Mi(d,r)
sigFa=signal_Fa(d,r)
sigSol=signal_Sol(d,r)

sigLaSi=signalLaSi(d,r)

sigDo1=signal_Do(d1,r)
sigMi1=signal_Mi(d1,r)


La=recadrage_for_scipy_16s_elvi(min(sigLa),max(sigLa),sigLa)
Si=recadrage_for_scipy_16s_elvi(min(sigSi),max(sigSi),sigSi)
Do=recadrage_for_scipy_16s_elvi(min(sigDo),max(sigDo),sigDo)
Re=recadrage_for_scipy_16s_elvi(min(sigRe),max(sigRe),sigRe)
Mi=recadrage_for_scipy_16s_elvi(min(sigMi),max(sigMi),sigMi)
Fa=recadrage_for_scipy_16s_elvi(min(sigFa),max(sigDo),sigFa)
Sol=recadrage_for_scipy_16s_elvi(min(sigSol),max(sigSol),sigSol)


Mi1=recadrage_for_scipy_16s_elvi(min(sigMi1),max(sigMi1),sigMi1)
Do1=recadrage_for_scipy_16s_elvi(min(sigDo1),max(sigDo1),sigDo1)

La_ns=recadrage_for_scipy_8ns_elvi(min(sigLa),max(sigLa),sigLa)
Si_ns=recadrage_for_scipy_8ns_elvi(min(sigSi),max(sigSi),sigSi)




DoDoDoReMiDo=np.concatenate((Do,Do,Do,Re,Mi1,Do1))

write('DoDoDoReMiDo.wav', 44100, DoDoDoReMiDo)


# =============================================================================
# Jouer en MONO
# =============================================================================
La_Si_mono_mixed=recadrage_for_scipy_16s_elvi(min(sigLaSi),max(sigLaSi),sigLaSi)
La_Si_mono_mixed_2moinsfort=recadrage_for_scipy_16s_elvi(min(sigLaSi),max(sigLaSi),sigLaSi*0.5) # ATTENTION MIN ET MAX NE CHANGENT PAS

La_Si_stereo=np.array([La,Si]).T # we need to transpose

# 1. Mixer La et Si en mono, note l'échantillon est sur 44100. Et nous on est en 44100*3, donc on est sur 3 secondes
write('La_Si_mono_mixed_16s.wav', 44100, La_Si_mono_mixed)
# 2. Jouer en 2 fois moins fort 
write('La_Si_mono_mixed_16s_2moinsfort.wav', 44100, La_Si_mono_mixed_2moinsfort)
# 3. Ecrire en stereo
write('La_Si_stereo_mixed_16s.wav', 44100, La_Si_stereo)



# =============================================================================
#  Son CONSTANT après un certain temps
# =============================================================================


d2=3
r=44100
fs=440
""" BEGIN TEST FUNCTION"""
sigLa=signal_La(d2,r)
def constant_after(signal,duration,rate):
    temps=np.linspace(0,duration,duration*rate)
#    sigLa=signal_La(duration,rate)
    s_La=[]
    for t in temps:
        if 0<=t<=1:
            s_La.append(signal*t)
        else:
            s_La.append(signal*1)
    return np.array(s_La)
            

s_La_function=constant_after(sigLa,d2,r)
La1=recadrage_for_scipy_16s_elvi(min(s_La_function),max(s_La_function),s_La_function)
write('La_constantaprest=1.wav', 44100, La1)
""" END TEST FUNCTION"""






temps=np.linspace(0,d2,d2*r)
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


La=recadrage_for_scipy_16s_elvi(min(s_La),max(s_La),s_La)
Si=recadrage_for_scipy_16s_elvi(min(s_Si),max(s_Si),s_Si)
La_Si_mono_mixed_constant=recadrage_for_scipy_16s_elvi(min(s_La_Si),max(s_La_Si),s_La_Si)


write('La_constantaprest=1.wav', 44100, La)
write('La_Si_mono_mixed_16s_sonconstantaprest=1.wav', 44100, La_Si_mono_mixed_constant)

# =============================================================================
#  Son qui decroit
# =============================================================================

d2=3
r=44100
fs=440

temps=np.linspace(0,d2,d2*r)
s_La=[]
s_Si=[]
for t in temps:
    if d2-1<=t<=d2:
        s_La.append(np.sin(2*np.pi*fs*t)*(d2-t))
        s_Si.append(np.sin(2*np.pi*fs*t*2**(2/12))*(d2-t))
    else:
        s_La.append(np.sin(2*np.pi*fs*t)*1)
        s_Si.append(np.sin(2*np.pi*fs*t*2**(2/12))*1)


s_La=np.array(s_La)
s_Si=np.array(s_Si)

s_La_Si=s_La+s_Si


La=recadrage_for_scipy_16s_elvi(min(s_La),max(s_La),s_La)
Si=recadrage_for_scipy_16s_elvi(min(s_Si),max(s_Si),s_Si)
La_Si_mono_mixed_constant=recadrage_for_scipy_16s_elvi(min(s_La_Si),max(s_La_Si),s_La_Si)


write('La_decroissantdernier1sec.wav', 44100, La)
write('LaSi_decroissantdernier1sec.wav', 44100, La_Si_mono_mixed_constant)













