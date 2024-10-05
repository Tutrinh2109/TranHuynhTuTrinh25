# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 16:04:53 2024

@author: TranHuynhTuTrinh
"""
# Tính S = 2 + 4 + 6 + ... + n (với n chẵn > 0)

n = int(input("Nhập số chẵn lớn hơn 0: "))
if n > 0 and n % 2 ==0:
    S = 0
    for i in range(2, n + 1, 2):
        S += i
    print(f"Tổng các số chẵn từ 2 đến {n} là: {S}")
else:
    print("Vui lòng nhập một số chẵn lớn hơn 0 hợp lệ!")
    