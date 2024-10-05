# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 13:13:55 2024

@author: TranHuynhTuTrinh
"""
"""
Viết chương trình tính tiền cước TAXI. Biết rằng: 1 km đầu tiên là 15000đ, 
từ km thứ 2 đến thứ 5 giá là 13500đ, từ km thứ 6 giá là 11000đ, nếu đi 
hơn 120km thì sẽ được giảm 10% trên tổng tiền
"""
km = float(input("Nhập số km đã đi: "))
tong_tien = 0
if km == 1:
    tong_tien = 15000
elif 2 <= km <= 5:
    tong_tien = 15000 + (km - 1) * 13500
elif km > 5:
    tong_tien = 15000 + 4 * 13500 + (km - 5) * 11000
elif km > 120:
    tong_tien *= 0.9  
print(f"Tổng tiền cước TAXI là: {tong_tien}đ")


