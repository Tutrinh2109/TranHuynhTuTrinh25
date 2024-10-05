# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 21:55:25 2024

@author: TranHuynhTuTrinh
"""

n = int(input("Nhập một số nguyên n: "))
dict = {i: i**i for i in range(1,n+1)}
print(dict)
