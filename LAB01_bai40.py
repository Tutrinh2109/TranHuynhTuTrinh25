# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 23:10:45 2024

@author: TranHuynhTuTrinh
"""

n = int(input("Nhập giá trị n: "))
S = 0
for i in range(1, n+1):
  S += 1 / (2 * i)
print(f"Tổng S = {S}")