# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 19:01:39 2024

@author: TranHuynhTuTrinh
"""
"""
Viết chương trình liệt kê tất cả bộ nghiệm nguyên của phương trình sau:
2x + 7y + 9z = 979 với x, y, z > 0 và x + y + z lớn nhất
"""
danh_sach = []
max = 0
for x in range(1, 490):
    for y in range(1, 140):
        for z in range(1, 109):
            if 2*x + 7*y + 9*z == 979:
                sum = x + y + z
                if sum > max:
                    max = sum
                    danh_sach += [(x,y,z)]
print(f"{danh_sach} với bộ nghiệm (x + y + z) = {max}")
