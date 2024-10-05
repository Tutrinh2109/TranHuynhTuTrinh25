# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 18:22:31 2024

@author: TranHuynhTuTrinh
"""
#1.Sử dụng vòng lặp for để lặp từ 0 đến 100 và in tổng tất cả các số.
print("Câu 1:")
tong = 0
for i in range(101):
    tong += i
print("Tổng: ", tong)
#2.Sử dụng vòng lặp for để lặp từ 0 đến 100 và in ra tổng của tất cả các số chẵn và tổng của tất cả các số lẻ.
print("Câu 2:")
tong_chan = 0
tong_le = 0

for i in range(101):  
    if i % 2 == 0:  
        tong_chan += i
    else:  
        tong_le += i
print("Tổng các số chẵn từ 0 đến 100 là:", tong_chan)
print("Tổng các số lẻ từ 0 đến 100 là:", tong_le)