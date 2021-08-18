#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 18 01:52:59 2021

@author: tb
"""
from Luas import luas
from Volume import volume
import math

unit = " cm"
d1 = 2*math.pi
d2 = 3
d3 = 1
vol = round(volume(d1,d2,d3),2)

print("Volume = "+str(vol)+unit+"³")
