# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 21:47:34 2024

@author: Nguyễn Thị Cẩm Nhung - 23712471
"""
a = int(input("Nhập số a: "))
b = int(input("Nhập số b: "))
c = int(input("Nhập số c: "))
if a > b:
    a, b = b, a
if a > c:
    a, c = c, a
if b > c:
    b, c = c, b
print(a, b, c)
