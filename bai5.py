# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 23:36:17 2024

@author: Nguyễn Thị Cẩm Nhung - 23712471
"""
h, m, s= map(int, input("Nhập thời gian theo định dạng hh:mm:ss:").split(":"))
tong =(h *3600)+(m *60)+s 
print("Tổng số giây:",tong )
