# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 19:29:05 2024

@author: TranHuynhTuTrinh
"""
#Viết chương trình in ra bản cửu chương 2 đến cửu chương 9.

for i in range(2, 10):  
        print(f"Bảng cửu chương {i}:")
        for j in range(1, 11): 
            print(f"{j} x {i} = {j * i}")
        print() 