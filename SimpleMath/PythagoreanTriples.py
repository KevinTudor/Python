# -*- coding: utf-8 -*-
"""
Spyder Editor

Kevin Tudor

HW1.1 Problem 2

Pythagorean Numbers:
 
The lengths (a,b,c) of the three sides of a right triangle are related 
by this well-known formula: a^2 + b^2 = c^2.

A Pythagorean triple consists of three positive integer numbers bound 
by the above relation. An example of a triple is (3,4,5) or (4, 3, 5).

displays to the terminal all possible Pythagorean triples (a,b,c).
"""

def find_Pythagorean(n): # (create a matrix) 111,112,113,121,122,123
    
    triples = []
    empty = 1 # True if list is empty
    num_triples = 0 # number of triples start 0 and increment by 2 if exists
    
    for a in range (1, n + 1): # 1 to n inclusive (1, 2, 3, 4, ... , n)
        for b in range (a, n + 1): # a to n inclusive (a, a + 1, a + 2,...,n)
            for c in range (b, n + 1):
                if (a**2 + b**2 == c**2):
                    # tuple uses round parenthesis and can’t be modified
                    triples.append(tuple([a, b, c])) 
                    triples.append(tuple([b, a, c])) #a^2 + b^2=b^2 + a^2=c^2
                    empty = 0 # False 
                    num_triples += 2 # add 2 possible triples to list counter
                    
    if(empty == 1 ): # list of tupples is empty (True)
        print("No possible pythagorean tripples for n = ", n)
    else: # list not empty (False)
        print(num_triples, "possible triples for n = ", n)
    
    return triples

cont = 0

while cont == 0:
    
    n_in = input("Enter positive ingeter n: ")
    n = int(n_in)
    
    if(n <= 0):
        print("invalid value, try again")
        cont = 0
    else:
        # display to the terminal all possible Pythagorean triples
        print ("Possible Pythagorean triples: ", find_Pythagorean(n)) 
        cont = 1
        
        
        