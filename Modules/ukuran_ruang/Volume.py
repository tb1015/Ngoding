#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 17 20:17:10 2021

@author: tb
"""
from Luas import luas

def volume(d1=1,d2=1,d3=1):
    """volume: fungsi untuk menghitung volume.
        d1: dimensi panjang 1
        d2: dimensi panjang 2
        d3: dimensi panjang 3"""
    
    return luas(d1,d2)*d3#print(str(luas(d1,d2)*d3)+" m³")

if __name__ == '__main__':    # kasus kondisional ini akan dieksekusi bila Volume.py dieksekusi ´
    print("fungsi volume") 