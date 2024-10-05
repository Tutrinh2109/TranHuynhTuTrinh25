# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 18:27:21 2024

@author: TranHuynhTuTrinh
"""
"""
Viết chương trình liệt kê tất cả bộ nghiệm nguyên của phương trình sau:
2x + 7y + 9z = 979 với (x, y, z > 0)
"""
danh_sach = []
for x in range(1, 490):
    for y in range(1, 140):
        for z in range(1, 109):
            if 2*x + 7*y + 9*z == 979:
                danh_sach += [(x,y,z)]
for i in danh_sach:
    print("Bộ nghiệm", i)

#Kiểm tra điều kiện của x,y,z:
while x<=0 and y<=0 and z<=0:
    print("Không hợp lệ")

    
                