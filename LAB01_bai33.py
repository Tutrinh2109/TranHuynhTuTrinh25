# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 13:32:36 2024

@author: TranHuynhTuTrinh
"""
"""
Viết chương trình nhập vào số nguyên dương n. Kiểm tra xem n có phải là 
số chính phương hay không? (Số chính phương là số khi lấy căn bậc 2 có 
kết quả là nguyên)
"""
import math
n = int(input("Nhập số nguyên dương n: "))
if n > 0:
    can_bac_hai = int(math.sqrt(n))
    if can_bac_hai * can_bac_hai == n:
        print(f"{n} là số chính phương.")
    else:
        print(f"{n} không phải là số chính phương.")
else:
    print("Vui lòng nhập một số nguyên dương hợp lệ!")
