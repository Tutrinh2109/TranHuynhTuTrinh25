# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 13:09:34 2024

@author: TranHuynhTuTrinh
"""
"""
Nhập vào ba số nguyên dương. Kiểm tra xem 3 số đó có lập thành tam giác 
không? Nếu có hãy cho biết tam giác đó thuộc loại nào? (Cân, vuông, 
đều...)
"""

a = int(input("Nhập cạnh a: "))
b = int(input("Nhập cạnh b: "))
c = int(input("Nhập cạnh c: "))
if a + b > c and a + c > b and b + c > a:
    print(f"Ba cạnh {a}, {b}, {c} lập thành một tam giác")
    if a == b == c:
        print("Là tam giác đều")
    elif a == b or b == c or a == c:
        if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
            print("Là tam giác vuông cân")
        else:
            print("Là tam giác cân")
    elif a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
        print("Là tam giác vuông")
    else:
        print("Là tam giác thường")
else:
    print("Không phải là tam giác")