# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 13:37:33 2024

@author: TranHuynhTuTrinh
"""
"""
Viết chương trình nhập vào số nguyên dương n. Kiểm tra xem n có phải là
số nguyên tố hay không
"""
import math
n = int(input("Nhập số nguyên dương n: "))
if n > 1:
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            print(f"{n} không phải là số nguyên tố")
            break
    else:
        print(f"{n} là số nguyên tố")
else:
    print(f"{n} không phải là số nguyên tố")
