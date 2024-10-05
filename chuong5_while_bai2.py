# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 20:08:02 2024

@author: TranHuynhTuTrinh
"""
"""
Viết lệnh kiểm tra giá trị nhập vào (phải là số thực) từ bàn phím
thỏa điều kiện thuộc [-89.9; 88.8]. Nếu không khỏa bắt người dùng
nhập lại đến khi nào khỏa điều kiện
"""
while True:
    number = float(input("Nhập vào một số thực: "))
    if number.is_integer():
      print("Vui lòng nhập số thực, không phải số nguyên.")
    elif -89.9 <= number <= 88.8:
      print("Số bạn nhập đã hợp lệ.")
      break
    else:
      print("Số bạn nhập không hợp lệ. Vui lòng nhập lại.")
      