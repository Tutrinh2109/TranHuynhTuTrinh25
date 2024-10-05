# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 12:13:16 2024

@author: TranHuynhTuTrinh
"""
"""
Tính tổng các chữ số N nguyên dương. (Nhập N = 6789 thì 6+7+8+9 = 30)
"""
N = int(input("Nhập vào một số nguyên dương N: "))
while N <= 0:
    print("N phải là số nguyên dương. Vui lòng nhập lại!")
    N = int(input("Nhập lại một số nguyên dương N: "))
tong = 0
for i in str(N):
    tong += int(i)
print(f"Tổng các chữ số của {N} là: {tong}")
