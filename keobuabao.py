# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 13:52:38 2024

@author: PC
"""
import random
choices = ["Kéo", "Búa", "Bao"]
computer = random.choice(choices)
player = input("Nhập lựa chọn của bạn (Kéo, Búa, Bao): ")
result = "Hòa!" if player == computer else (
    "Bạn thắng!" if (player, computer) in [("Kéo", "Bao"), ("Búa", "Kéo"), ("Bao", "Búa")] else "Máy thắng!"
)
print(f"Bạn chọn {player} và máy chọn {computer}. {result}")
