#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 09:38:07 2020

@author: egovenda
"""
"""TP : Exercice 1,
        and references: 
            - https://medium.com/@nickolasteixeira/how-to-explain-to-my-wife-what-i-do-how-do-you-get-the-maximum-and-minimum-values-for-integer-befdc263a3a2
            https://www.devdungeon.com/content/working-binary-data-python
"""

import struct

"""Part a"""

"""Max and Min of Unsigned 8bits integer"""
int_max_8=pow(2,8)-1

"""Max and Min of Unsigned 16bits integer"""
int_max_16=pow(2,16)-1

"""Max and Min of signed 8bits integer"""
int_min_8s=(pow(2,8)/2)*-1
int_max_8s=(pow(2,8)/2)-1

"""Max and Min of signed 8bits integer"""
int_min_16s=(pow(2,16)/2)*-1
int_max_16s=(pow(2,16)/2)-1


"""Part b"""
number=256
a_bytes_big=number.to_bytes(2,'big')
print(a_bytes_big)
a_bytes_little=number.to_bytes(2,'little')
print(a_bytes_little)


print(int.from_bytes(b'\x00\x01', "big"))
print(int.from_bytes(b'\x00\x01', "little")) 
print(int.from_bytes(b'\x00\x10', byteorder='little'))
print(int.from_bytes(b'\xfc\x00', byteorder='big', signed=True))

"""Part c"""
"""Writing txt file in python with bytes values"""
bytes1=b"\xDE\xAD\xBE\xEF"
liste=[1,2,3,5,4]
bytes2=bytes(liste)

f=open("tp1.txt","wb")
f.write(bytes2)
f.close()


"""Reading txt file in python with bytes values"""

byte_list=[]

with open("tp1.txt","rb") as f:
    while True:
        #byte=f.read() #reads whole line
        byte=f.read(1) #reads individual word
        if not byte:
            break
        byte_list.append(byte)
print(byte_list)

for byte in byte_list:
    int_value = ord(byte)
    
    binary_string = '{0:08b}'.format(int_value)
    print(binary_string)


"""Part d"""
liste1=[1,2,3,4,5,6,7,8,9,10]

f1=open("f8u.bin","wb")
for items in liste1:
    f1.write(items.to_bytes(1,"big")) # Ici on ecrit avec 1 octet (8 bits)
f1.close()

bytet_list=[]
int_list=[]
with open("f8u.bin","rb") as f1:
    while True:
        #byte=f.read() #reads whole line
        bytet=f1.read(2) #reads 2 words since it is in 2 octets
        if not bytet:
            break
        bytet_list.append(bytet)
        int_list.append(int.from_bytes(bytet,"big"))
print(bytet_list)
print(int_list)


"""Part e"""
liste2=[1,2,3,4,5,6,7,8,9,324]

f2=open("f16sl.bin","wb")
for items in liste2:
    f2.write(items.to_bytes(2,"little",signed=True)) # Ici on ecrit avec 2 octet (16 bits)
f2.close()

bytet_list1=[]
int_list1=[]
with open("f16sl.bin","rb") as f2:
    while True:
        #byte=f.read() #reads whole line
        bytet1=f2.read(2) #reads 2 words since it is in 2 octets
        if not bytet1:
            break
        bytet_list1.append(bytet1)
        int_list1.append(int.from_bytes(bytet1,"little",signed=True))
print(bytet_list1)
print(int_list1)

"""Part f"""
liste3=[1,2,3,4,5,6,7,8,9,258]

f3=open("f16sb.bin","wb")
for items in liste3:
    f3.write(items.to_bytes(2,"big",signed=True)) # Ici on ecrit avec 2 octet (16 bits)
f3.close()

bytet_list2=[]
int_list2=[]
with open("f16sb.bin","rb") as f3:
    while True:
        #byte=f.read() #reads whole line
        bytet2=f3.read(2) #reads 2 words since it is in 2 octets
        if not bytet2:
            break
        bytet_list2.append(bytet2)
        int_list2.append(int.from_bytes(bytet2,"big",signed=True))
print(bytet_list2)
print(int_list2)


"""Part g"""
liste4=[-0.5,-1.7,2,3]

f4=open("ffloat.bin","wb")
for items in liste4:
    f4.write(items.to_bytes(2,"big",signed=True)) # Ici on ecrit avec 2 octet (16 bits)
f4.close()

bytet_list3=[]
int_list3=[]
with open("ffloat.bin","rb") as f4:
    while True:
        #byte=f.read() #reads whole line
        bytet3=f4.read(2) #reads 2 words since it is in 2 octets
        if not bytet3:
            break
        bytet_list3.append(bytet3)
        int_list3.append(int.from_bytes(bytet3,"big",signed=True))
print(bytet_list3)
print(int_list3)