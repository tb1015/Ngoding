#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 10 11:08:31 2021

https://scikit-learn.org/stable/getting_started.html

@author: tb
"""

# Fitting and predicting: estimator basics
from sklearn.ensemble import RandomForestClassifier

clf = RandomForestClassifier(random_state=0)
X = [[1,2,3],
     [11,12,13]] # 2 samples, 3 features

y = [0,5] # classes of each sample

clf.fit(X,y)
#print(clf)

clf.predict(X)

clf.predict([[4,5,6], [14,15,16]])

clf.predict([[4,15,6]])

