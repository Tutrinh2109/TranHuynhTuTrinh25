# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 21:35:21 2024

@author: TranHuynhTuTrinh
"""
"""
Viết chương trình tạo một danh sách tự động các số chẵn nguyên
từ 2020 đến 3838.
1. Tạo danh sách các số chia hết cho 9 từ danh sách thu
được.
2. Các số thu được sẽ được in thành chuỗi trên một dòng,
cách nhau bằng 1 tab
"""
#Tạo danh sách các số chẵn từ 2020 đến 3838
danh_sach_chan = [so for so in range(2020, 3839) if so % 2 == 0]
#1.Tạo danh sách các số chia hết cho 9 từ danh sách chẵn
danh_sach_chia_het_cho_9 = [so for so in danh_sach_chan if so % 9 == 0]
print("Danh sách các số chẵn chia hết cho 9 là: ")
#2.In các số thu được thành chuỗi trên một dòng, cách nhau bằng 1 tab
for so in danh_sach_chia_het_cho_9:
    print(so, end="\t")
