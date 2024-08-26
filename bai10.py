# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 13:05:41 2024

@author: Nguyễn Thị Cẩm Nhung - 23712471
"""
from math import factorial
from collections import Counter
def count(number):
    x = Counter(number)
    total = factorial(len(number))
    for i in x.values():
        total //= factorial(i)
    return total
number = input("Nhập biển số xe 4 số: ")
print(f"Số nút của biển số xe {number} là: {count(number)}")
