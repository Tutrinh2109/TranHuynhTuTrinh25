# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 19:12:36 2024

@author: TranHuynhTuTrinh
"""
#1.In từ 0 đến 10 bằng vòng lặp for và while.
print("Câu 1:")
for i in range(11):
    print(i)
i = 0
while i <= 9:
    i += 1
    print(i)
print("Câu 2:")
#2.In lại từ 10 đến 0 bằng vòng lặp for và while.
for i in range(10, -1, -1):
    print(i)
i = 10
while i >=0:
    print(i)
    i -= 1
print("Câu 3:")
#3.Dùng vòng lặp để vẽ hình số 1.
for i in range(7):
    print('#' * 7)
print("Câu 4:")
#4.Dùng vòng lặp để in bảng cửu chương như hình số 2.
for i in range(11):
     print(f"{i} x {i} = {i * i}")
print("Câu 5:")
#5.Dùng for để lặp từ 0 đến 100 và chỉ in các số chẵn.
for i in range(101):
    if i % 2 == 0 :
        print(i)
print("Câu 6:")
#6.Làm tương tự câu trên nhưng là in số lẻ.
for i in range(101):
    if i % 2 != 0:
        print(i)