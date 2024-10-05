# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 16:12:56 2024

@author: TranHuynhTuTrinh
"""
#Tính S = 1 * 2 * 3 * ... * n (với n lẻ > 0)

n = int(input("Nhập số lẻ lớn hơn 0: "))
if n > 0 and n % 2 != 0:
    S = 1
    for i in range(1, n + 1):
        S *= i
    print(f"Tích các số từ 1 đến {n} là: {S}")
else:
    print("Vui lòng nhập một số lẻ lớn hơn 0 hợp lệ!")
