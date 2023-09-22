# -*- coding: utf-8 -*-
"""
Spyder Editor

Kevin Tudor

Problem 2

recursion
"""

from turtle import *
import turtle


def draw_leaf_straight(level, length): #2a

    if (level == 1):
        
        if (level <= 0):
            return
        
        forward(length/2)
        left(45)
        forward(length/6)
        backward(length/6)
        
        right(90)
        forward(length/6)
        backward(length/6)
        
        left(45)
        forward(length/2)
        backward(length)
    
    else:
        
        if (level <= 0):
            return
            
        forward(length)
            
        left(45)
        draw_leaf_straight(level - 1, length/4) # left branch
        right(45)
        draw_leaf_straight(level - 1, (length/2) + (level/2)) # middle branch
        right(45)
        draw_leaf_straight(level - 1, length/4) #right branch
        left(45)
            
        backward(length)
    
        return
    
    
def draw_leaf_curved(level, length): #2a extra credit
        
    if (level <= 0): # base case
        return
    
    forward(length)
    
    left(45)
    draw_leaf_curved(level - 1, length/4) # left branch
    right(60)
    draw_leaf_curved(level - 1, (length/2) + (level/2)) # middle branch
    right(45)
    draw_leaf_curved(level - 1, length/4) #right branch
    left(60)
            
    backward(length)
    
    return    


def test_leaf(): #test 2a
    
    left(90)
    turtle.speed(0)
    #turtle.delay(0)
    #draw_leaf_straight(1, 120)
    #draw_leaf_straight(6, 120)
    draw_leaf_curved(6, 120)
    
    turtle.done()
    try:
        turtle.bye()   
    except turtle.Terminator:
        pass
    

""" (Part 2B)
Convert a non-negative int value n to a string representation of n
in the given base. The base parameter is an int between 2 and 26.
For digits greater than 9 use letters ‘A’-’Z’. 
"""  
def strB(n, base = 0):
    
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" #values for numbers > 9 in base 10+ 
    
    if n < 0:
        raise ValueError("Number: " + str(n) + ", out of range [0 to infinity]")

    if n < 1 and base != 0:  #base case if n < 1 and base is given
        return ''
    
    elif n == 0 and base == 0: #base case if n == 0 and base is not given
        return 0
    
    if base < 2 or base > 26: #raise error if base out of range
        raise ValueError("Base: " + str(base) + ", out of range [2 to 26]")
            
    #recursive argument
    oper = n//base 
    #print("operation: ", oper)
    
    result = n%base
    if result > 9:
        alpha_num = result - 9
        result = alphabet[alpha_num-1]
    #print("result: ", result)

    return str(strB(oper,base)) + str(result)        

    
def Cnk(n,k): #no memoization
    
    if k > n: # input error checking
        raise ValueError(str(k) + "(k) > " + str(n) + "(n) value")
        
    if n == k or k == 0: # base cases
        return 1
        
    #recursive arguments
    n_fac = 1
    for x in range(1, n + 1):
        n_fac *= x
    #print(n, "factorial:", n_fac)
            
    k_fac = 1
    for y in range(1, k + 1):
        k_fac *= y
    #print(k, "factorial:", k_fac)   
            
    nmk_fac = n - k
    for z in range(1, nmk_fac):
        nmk_fac *= z
    #print(n, "-", k, "=", n-k, "factorial:", nmk_fac)
            
    #comb = n_fac / (k_fac * nmk_fac)
        
    return (Cnk(n-1, k-1) + Cnk(n-1, k))
    
def Cnk_m(n,k): #memoization
    
    if (n,k) not in Cnk_dict and k >= 0:
        
        if k > n: # input error checking
            raise ValueError(str(k) + "(k) > " + str(n) + "(n) value")
            
        if n == k or k == 0: # base cases
            return 1
        
        #recursive arguments
        n_fac = 1
        for x in range(1, n + 1):
            n_fac *= x
        #print(n, "factorial:", n_fac)
            
        k_fac = 1
        for y in range(1, k + 1):
            k_fac *= y
        #print(k, "factorial:", k_fac)   
            
        nmk_fac = n - k
        for z in range(1, nmk_fac):
            nmk_fac *= z
        #print(n, "-", k, "=", n-k, "factorial:", nmk_fac)
            
        #comb = n_fac / (k_fac * nmk_fac)
        Cnk_dict[(n,k)] = (Cnk_m(n-1, k-1) + Cnk_m(n-1, k))
        
    return Cnk_dict[(n,k)]

#"Global" n choose k dictionary
Cnk_dict = {}     
#base cases
Cnk_dict[(1, 1)] = 1
Cnk_dict[(1, 0)] = 1

lst = []

def make_pairs(seq1, seq2):
    
    temp_s1 = seq1
    temp_s2 = seq2
    
    if (not seq1 or not seq2): #check if empty
        return []
  
    lst.append((seq1[0], seq2[0]))
        
    temp_s1.remove(temp_s1[0])
    temp_s2.remove(temp_s2[0])
    
    
    if (len(temp_s1) == 0 or len(temp_s2) == 0):

        return lst

    return make_pairs(temp_s1, temp_s2)

    
def test_b_to_d():
    
    #part b (base conversion)
    print("-----------------PART b-------------------")
    print(strB(0)) #0
    #print(strB(-1)) #ValueError
    #print(strB(998, base = 0)) #ValueError
    print(strB(1200, base=11)) #9A1
    print(strB(1201, base=12)) #841
    print(strB(1202, base=13)) #716
    print(strB(1203, base=14)) #61D
    print(strB(1234, base=10)) #1234
    print(strB(10, base=8)) #12
    print(strB(100, base=8)) #144
    print(strB(100, base=16)) #64
    print(strB(1024, base=16)) #400
    print(strB(15, base=13)) #12
    print(strB(15, base=25)) #F
    print(strB(123, base=16)) #7B
    print(strB(1234, base=16)) #4D2
    print(strB(8191, base=16)) #1FFF
    print(strB(100, base=13)) #79
    print(strB(102, base=13)) #7B
    print(strB(123456789, base=26)) #AA44A1
    print(strB(16, base=2)) #10000
    print(strB(100, base=2)) #1100100
    
    
    #part c (binomial coefficients)
    print("-----------------PART c-------------------")
    #print(Cnk(30, 10))   # 42 seconds AWFUL!
    #print(Cnk_m(100, 10))   # <1 seconds AMAZING
    #print(Cnk_dict)
    
    #part d (pairs)
    print("-----------------PART d-------------------")
    print(make_pairs([1,2,3], [4,5,6])) #[(1, 4), (2, 5), (3, 6)]
    lst.clear()
    print(make_pairs([1,2,3], [4,5])) #[(1, 4), (2, 5)]
    lst.clear()
    print(make_pairs([1,2,3], [4,5,6,7,8,9])) #[(1, 4), (2, 5), (3, 6)]
    lst.clear()
    print(make_pairs([], [4,5,6,7,8,9])) #[]
    lst.clear()
    print(make_pairs([1,2,3], [4])) #[(1, 4)]
    lst.clear()
    print(make_pairs([1,2,3], [])) #[]
    
    
def main():
    
    test_leaf()
    #test_b_to_d()

print("-----------------------------------------------------")
    
if (__name__=="__main__"):
    main()


print("-----------------------------------------------------")


"""
NOTES:
    
    for problem 2b
    base conversion method found on 
    https://www.tutorialspoint.com/computer_logical_organization/number_system_conversion.htm
    
    for problem 2c
    memoized binomial coeffecient method found on 
    https://en.wikipedia.org/wiki/Combination

    
"""