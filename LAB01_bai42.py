# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 23:22:51 2024

@author: ASUS
"""
n = int(input("Nhập giá trị n: "))
S = 0
for i in range(1, n+1):
  S += 1 / (i * (i + 1))
print(f"Tổng S = {S}")
