# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 19:11:08 2024

@author: TranHuynhTuTrinh
"""
"""
Viết chương trình liệt kê tất cả bộ nghiệm nguyên của phương trình sau:
2x + 7y + 9z = 979 với x, y, z > 0 và x + y + z nhỏ nhất
"""

danh_sach = []
min = 979
for x in range(1, 490):
    for y in range(1, 140):
        for z in range(1, 109):
            if 2*x + 7*y + 9*z == 979:
                sum = x + y + z
                if sum < min:
                    min = sum
                    danh_sach += [(x,y,z)]
print(f"{danh_sach} với bộ nghiệm (x + y + z) = {min}")
