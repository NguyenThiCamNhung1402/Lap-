# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 15:13:25 2024

@author: Nguyễn Thị Cẩm Nhung - 23712471
"""
a, b, c, d = map(int, input("Nhập 4 số nguyên (cách nhau bằng khoảng trắng): ").split())
if a < b and a < c and a < d:
    m = a
elif b < c and b < d:
    m= b
elif c < d:
    m = c
else:
    m = d
print("Số nhỏ nhất:", m )
