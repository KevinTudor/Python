# -*- coding: utf-8 -*-
"""
Spyder Editor

Kevin Tudor

HW1.1 Problem 3

Duplicated Substrings:
    
    a) Write in file p3_….py a function find_dup_str(s, n) that determines 
whether a string s contains a duplicated substring of a given length
n and that returns the first occurring substring of length n that 
is duplicated (if any) or the empty string, otherwise. For the example
above (s == “abcdefbcdgh”) with substring length 3, the substring to be
returned is “bcd“. With length 2, the algorithm returns “bc”, and not “cd”.
For this value of parameter s, if the length parameter is 4 or more, the
algorithm returns “”. Your solution must use string slicing and must not
use function str.

Write after the function definition some code that reads a string and a 
number from the terminal, and then calls find_dup_str(s, n) and prints the
result. Use this for testing.

    b) Write in file p3_….py a function find_max_dup(s) that takes a string s
as parameter and that determines the longest substring that is duplicated 
in s. For instance, find_max_dup(“abcdefbcdgh”), the function should return 
“bcd”. If the string s has no duplicated substrings, then the algorithm should 
return the empty string, e.g. find_max_dup(“0123456”) should return “”.
This function MUST use the code written for part b), i.e. must make calls 
to find_dup_str(…) and use its result.

Write after the function definition code that reads a string from the 
terminal in variable s and then calls find_max_dup(s) and prints the result. 

"""

def find_dup_str(s, n):
    
    dub_str = []
    dub_count = 0
    
    for x in range (0, len(s)-1):
        dub_str.append(s[x:x + n])
        
    #print ("\nList:", dub_str)
        
    for y in range (0, len(dub_str)-1):
        if (dub_count == 1):
            break
        for z in range (y + 1, len(dub_str)):
            if (dub_str[y] == dub_str[z]):
                dub_count += 1
                return (dub_str[y])          
                
    if (dub_count == 0):
       return ""
       

def find_max_dup(s):
    
    for x in range (len(s), 0, -1):
        
        if (find_dup_str(s,x) != ""):
            return find_dup_str(s,x)  

cont = 0

while cont == 0:
    
    s = input("Enter a string: ")
    
    if (s == ''):
        break
    
    n_in = input("Enter a substring length: ")
    n = int(n_in)
    
    if (n > len(s)):
        print("Invalid value, try again")
        break
    
    print ("\nFirst duplicated value: ", find_dup_str(s,n))
    print ("\nMax duplicated value: ", find_max_dup(s))



















