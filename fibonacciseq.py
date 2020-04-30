# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 09:39:20 2020

@author: Julie
"""

#prompt user for number of terms for sequence
n = int(input("How many terms?"))
#define terms
a = 0
b = 1
sum = 0
count = 1   
print("Fibonacci sequence:")   
while(count <= n):
         print(sum)
         count += 1
         a = b
         b = sum
         sum = a + b
     
    