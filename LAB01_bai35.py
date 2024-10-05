# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 15:21:37 2024

@author: TranHuynhTuTrinh
"""
#Tính S = 1 + 2 + 3 + ... + n (n nguyên và lớn hơn 0)

n = int(input("Nhập số nguyên dương n: "))
if n > 0:
    S = 0
    for i in range(1, n + 1):
        S += i
    print(f"Tổng S = 1 + 2 + 3 + ... + {n} là: {S}")
else:
    print("Vui lòng nhập một số nguyên dương hợp lệ!")