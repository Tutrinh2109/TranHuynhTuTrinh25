# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 18:02:53 2024

@author: TranHuynhTuTrinh
"""
"""
Viết chương trình có thể tạo danh sách:
• Số lượng các phần tử được chọn ngẫu nhiên từ 20 đến 30.
• Các giá trị bình phương của các số thực được chọn ngẫu nhiên
từ 18 đến 99.
"""

import random
# Số lượng phần tử được chọn ngẫu nhiên từ 20 đến 30
so_luong = random.randint(20, 30)
# Tạo danh sách các giá trị bình phương của các số thực ngẫu nhiên từ 18 đến 99
binh_phuong = [(random.uniform(18, 99))**2 for _ in range(so_luong)]
# In danh sách kết quả
print(f"Số lượng phần tử: {so_luong}")
print("Danh sách các giá trị bình phương:")
for i in binh_phuong:
    print(i)