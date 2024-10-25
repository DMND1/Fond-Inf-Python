# -*- coding: utf-8 -*-
"""
Created on Wed Sep  5 14:45:36 2018

Dato un intero, il programma visualizza la sequenza di interi fino
ad 1 secondo la congettura di Collatz

@author: gabriele
"""

n = int(input("Inserisci un numero naturale: "))

while n > 1:
    print(n)
    if n % 2 == 0:
        n = n // 2
    else:
        n = 3*n +1

print(n)