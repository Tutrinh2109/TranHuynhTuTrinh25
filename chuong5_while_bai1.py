# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 20:00:22 2024

@author: TranHuynhTuTrinh
"""
"""
Viết lệnh kiểm tra giá trị nhập vào từ bàn phím thỏa điều kiện thuộc
[-99; 99]. Nếu không khỏa bắt người dùng nhập lại đến khi nào
khỏa điều kiện
"""
while True:
  number = int(input("Nhập vào một số nguyên: "))
  if -99 <= number <= 99:
    print("Số bạn nhập đã hợp lệ.")
    break
  else:
    print("Số bạn nhập không hợp lệ. Vui lòng nhập lại.")
