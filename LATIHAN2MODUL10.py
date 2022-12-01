#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 17:13:34 2022

@author: sonyaridesia
"""

def tukar(A, i, j):
    temp = A[i]
    A[i] = A[j]
    A[j] = temp
    
def bubbleSort(A, n):
    for i in range(n - 1):
        if A[i] > A[i + 1]:
            tukar(A, i, i + 1)
    if n - 1 > 1:
        bubbleSort(A, n - 1)
        
A = [1, 3, 6, 7, -2, 4, -8]
bubbleSort(A, len(A))
print("List yang sudah disorting")
print(A)