# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 19:15:20 2024

@author: TranHuynhTuTrinh
"""
"""
Viết chương trình tính giai thừa của một số cho trước n (nguyên 
dương) được nhập từ bàn phím.
S = n! = 1.2.3...n
"""

# Nhập số nguyên dương n từ bàn phím
n = int(input("Nhập số nguyên dương n: "))

# Khởi tạo giá trị ban đầu cho giai thừa
bien = 1

# Kiểm tra nếu n lớn hơn 0
if n > 0:
    for i in range(1, n + 1):
        bien *= i
    print(f"Giai thừa của {n} là: {bien}")
else:
    print("Vui lòng nhập một số nguyên dương.")