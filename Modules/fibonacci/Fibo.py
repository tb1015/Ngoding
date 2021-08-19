#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 19 12:34:23 2021

@author: tb
"""
# Fibonacci numbers module

def fib(n):    # write Fibonacci series up to n
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b # a=b, b=a+b
    print()

def fib2(n):   # return Fibonacci series up to n
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result


if __name__ == "__main__": #If the Fibo function is used / run as a main script, then do:
    import sys # Importing all definitions and statements in this module (Fibo)
    fib(int(sys.argv[1])) # Reading system argument given by the user, and inserting the arg-value into fib() function