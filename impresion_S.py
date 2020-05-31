# -*- coding: utf-8 -*-
"""
Created on Thu May  7 07:52:11 2020

@author: EstAnthonyFabricioSa
"""
sw=[]
devices=["R1","R2","R3","S1","S2","S3","S4","S5"]
for i in devices:
    if "S" in i:
            sw.append(i)        
print(sw)
    

