# -*- coding: utf-8 -*-
"""
Spyder Editor

Kevin Tudor

Homework 5 (functional programming)

Problem 1

Random Number Generator

"""

#part a -> Iterator Class (FP element in Python)
""" a class called RndSeq

generates the sequence of n pseudo-random numbers starting with a 
seed value x0, where n and x0 are given as parameter to the constructor
 
"""
class RndSeq(object):
    
    """ default constructor
    
    initialize given values and necessary counters
    
    """
    def __init__(self, x0, n):
        
        self.m = 2**32
        self.a = 22695477
        self.c = 1
        
        self.x0 = x0
        self.n = n
        
        self.counter = 0  #used to determine amount of pseudo random numbers created

    
    """ name: iterator interface
    
    returns the iterator object reference
    
    """
    def __iter__(self):
        
        return self
        
    """ name: next method
    
    lazily creates and returns the next object in the "sequence"
    if n > 0 create n pseudo random numbers
    if n < 0 create infinite pseudo random numbers
    
    """
    def __next__(self): #lazy computation
        
        if self.n > 0:
            
            self.counter += 1
            ret = (self.a * self.x0 + self.c)%self.m
            self.x0 = ret
            
            if self.counter > self.n:
                raise StopIteration
            
            return ret
        
        else:
            while True: #generate infinite pseudo random numbers
                
                #self.counter += 1         #error checking
                
                ret = (self.a * self.x0 + self.c)%self.m
                self.x0 = ret
                print(ret)
                #return ret                #infinite list
                #if self.counter == 5:     #error checking
                    #raise StopIteration   #error checking
 
def part_a():
    
    #first option
    print("First option")
    rnd = RndSeq(1, 10)
    print([i for i in rnd])  #for is suppported
        
    #second option
    print("\nSecond option")
    rnd = RndSeq(1, 2) #RndSeq(x0(seed value),n(amount of pseudo-random nums))
    it = iter(rnd)
    print(next(it))  #next is supported
    print(next(it))
    print(next(it))  #raises exception "StopIteration", n = 2


def rnd_gen(x0,n):
    
    m = 2**32
    a = 22695477
    c = 1
    
    counter = 0  #used to determine amount of pseudo random numbers created
    
    if n >= 0:
        while counter < n:  
            
            ret = (a * x0 + c)%m
            x0 = ret
            yield ret
            counter += 1
        
    else:
        while True: #generate infinite pseudo random numbers
                
            #counter += 1         #error checking
                
            ret = (a * x0 + c)%m
            x0 = ret
            #print(ret)
            yield ret                 #generates infinite list
                
            #if counter == 5:     #error checking
                #raise StopIteration   #error checking

def part_b():
    
    print("First option")
    print([i for i in rnd_gen(1, 10)])  #for is suppported
    print("\nSecond option")
    print(list(rnd_gen(1, 3)))
    print("\nCreating and printing lists with the first 10 random numbers with seed 2")
    print([i for i in rnd_gen(2, 10)])  #for is suppported

def main():
    
    #part_a()
    part_b()


print("-----------------------------------------------------")
    
if (__name__=="__main__"):
    
    main()


print("-----------------------------------------------------")


"""
NOTES:
    
iterator represents a stream of data items.   
    outputs an item one at a time.
    Provides support for implementing the for statement
    
seed(n): sets seed
seed(): sets seed from system clock
randint(a,b): generates random a<=int<=b
random(): generates random 0<=float<1
choice(sequence): selects random element
shuffle(sequence): shuffles elements in-place
sample(sequence, num): returns new random sequence with num samples, without replacement
Distributions: betavariate, expovariate, gammavariate, gauss, lognormvariate, normalvariate, paretovariate, randrange



"""