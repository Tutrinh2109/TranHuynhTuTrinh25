# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 12:33:51 2024

@author: TranHuynhTuTrinh
"""
"""
Viết chương trình nhập vào tháng năm. Hãy cho biết tháng đó có bao nhiêu 
ngày?
"""
thang = int(input("Nhập tháng (1-12): "))
nam = int(input("Nhập năm: "))
nam_nhuan = (nam % 4 == 0 and nam % 100 != 0) or (nam % 400 == 0)
if thang in [1, 3, 5, 7, 8, 10, 12]:
    print(f"Tháng {thang} năm {nam} có 31 ngày.")
elif thang in [4, 6, 9, 11]:
    print(f"Tháng {thang} năm {nam} có 30 ngày.")
elif thang == 2:
    print(f"Tháng 2 năm {nam} có {29 if nam_nhuan else 28} ngày.")
else:
    print("Tháng không hợp lệ!")