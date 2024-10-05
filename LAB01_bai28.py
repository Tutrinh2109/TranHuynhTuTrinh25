# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 12:10:36 2024

@author: TranHuynhTuTrinh
"""
"""
Nhập vào số N từ bàn phím (điều kiện N nguyên dương) nếu người dùng 
nhập không đúng thì bắt nhập lại. Sao đó in ra tất cả ước số của N.
"""

N = int(input("Nhập số nguyên dương N: "))
while N <= 0:
    print("N phải là số nguyên dương. Vui lòng nhập lại!")
    N = int(input("Nhập lại số nguyên dương N: "))
print(f"Các ước số của {N} là:")
for i in range(1, N + 1):
    if N % i == 0:
        print(i)