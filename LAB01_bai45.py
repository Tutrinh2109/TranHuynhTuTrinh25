# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 23:27:07 2024

@author: TranHuynhTuTrinh
"""
x = float(input("Nhập giá trị x: "))
n = int(input("Nhập giá trị n: "))
S = 0
for i in range(1, n + 1):
    mau = 0
    for j in range(1, i + 1):
        mau += j 
    S += (x ** i) / mau
print(f"Tổng S = {S}")