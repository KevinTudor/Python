# -*- coding: utf-8 -*-
"""
Spyder Editor

Kevin Tudor

HW1.1 Problem 2 (Including graph)

Pythagorean Numbers:
 
I decided to give myself extra practice by graphing this problem as well

"""
import matplotlib.pyplot as graph


def find_num_triples(x):
    
    num_triples = 0 # number of triples starts as 0 and increments by 2 if any exists
    
    for a in range (1, x + 1): # 1 to n inclusive (1, 2, 3, 4, ... , n)
        for b in range (a, x + 1): # a to n inclusive (a, a + 1, a + 2, ... , n)
            for c in range (b, x + 1):
                if (a**2 + b**2 == c**2):
                    num_triples += 2 # add 2 possible triples to list counter

    return int(num_triples)

def find_Pythagorean(n): # (create a matrix) 111,112,113,121,122,123
    
    triples = []
    empty = 1 # True if list is empty
    num_triples = 0 # number of tripples starts as 0 and increments by 2 if any exists
    
    for a in range (1, n + 1): # 1 to n inclusive (1, 2, 3, 4, ... , n)
        for b in range (a, n + 1): # a to n inclusive (a, a + 1, a + 2, ... , n)
            for c in range (b, n + 1):
                if (a**2 + b**2 == c**2):
                    # tuple uses round parenthesis and can not be modified
                    triples.append(tuple([a, b, c])) 
                    triples.append(tuple([b, a, c])) # a^2 + b^2 = b^2 + a^2 = c^2
                    empty = 0 # False 
                    num_triples += 2 # add 2 possible triples to list counter
                    
    if(empty == 1 ): # list of tupples is empty (True)
        print("No possible pythagorean tripples for n = ", n)
    else: # list not empty (False)
        print(num_triples, "possible triples for n = ", n)
        
        # initialize the lists
        xs = []
        ys = []
        
        # prepare the domain for the function we graph
        lb = 0
        ub = n
        
        # starting (left) value
        x = lb         
        
        #populate xs
        while x <= ub: 
            xs.append(x) #add element at the end of the list (push back)
            
            #populate ys
            if (x == 0 or x == 1 or x == 2 or x == 3):
                y = 0
            else:
                y = find_num_triples(x)
                
            ys.append(y)
            
            #increment x
            x += 1
       
        # after the loop: fill out plot
        graph.plot(xs, ys, "ro-")   # creates the graph figure, doesn't show yet
        graph.title("Number of triples for n: " + str(n))     # title
        graph.xlabel("n")                                     # x label
        graph.ylabel("number of triples")                     # y label
        graph.show()                                          # show plot
    
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
        


