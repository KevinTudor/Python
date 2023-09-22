# -*- coding: utf-8 -*-
"""
Spyder Editor

Kevin Tudor

Homework 5 (Functional Programming)

Problem 2. Functional Programming

"""

from itertools import islice, filterfalse
from functools import reduce

def rnd_gen(x0,n):
    
    m = 2**32
    a = 22695477
    c = 1
    
    counter = 0  #used to determine amount of pseudo random numbers created
    
    if n >= 0:
        while counter < n:  
            counter += 1
            ret = (a * x0 + c)%m
            x0 = ret
            
            yield ret
        
    else:
        while True: #generate infinite pseudo random numbers
                
            #counter += 1              #error checking
                
            ret = (a * x0 + c)%m
            x0 = ret
            #print(ret)
            yield ret                  #generates infinite list
                
            #if counter == 5:          #error checking
                #raise StopIteration   #error checking

#part a
def gen_rndtup(m):
    
    it = iter(rnd_gen(1,-1))
    
    while True:
        
        a = next(it)%m
        b = next(it)%m
        
        if b >= a:
            yield ((a,b))
            

def main():
    
    print("Part a")
    #[print(i) in i for i in gen_rndtup(10)] #infinite
    
    print("\nPart b")
    filter_eight = islice(filterfalse(lambda x: x[0] + x[1] <= 6, gen_rndtup(10)), 0, 8)
    [print(i) in i for i in filter_eight]
    
    print("\nPart c")
    #it_a = iter(rnd_gen(1,-1))
    it_b = iter(rnd_gen(2,-1))
    
    a_lst, b_lst, filter_ab = [], [], []
    
    for a in rnd_gen(1, -1):
        a = a%100
        b = next(it_b)%100
        if a <= b:
            #print(a,b)
            a_lst.append(a)
            b_lst.append(b)
        if len(a_lst) >= 8:
            filter_ab = zip(a_lst,b_lst)
            break       
    [print(i) in i for i in filter_ab]
    
    print("\nPart d")  #between 0 to 100
    #including zero?
    #result = islice(filter(lambda x: x % 13 == 0, map(lambda y: y % 100, rnd_gen(1, -1))), 10)
    
    #not including zero
    result = islice(filter(lambda x: x != 0 and x % 13 == 0, map(lambda y: y % 100, rnd_gen(1, -1))), 10)
    
    for x in result:
        print(x)
        
    print("\nPart e")
    #sum_ten = reduce(lambda a, b: a + b, islice(filter(lambda y: y[0] + y[1] >= 5, gen_rndtup(10)), 10))
    sum_ten = reduce(lambda a, b: a + b, #reduce tuples
                     map(lambda x: x[0] + x[1], #add up each portion of all tuples
                         islice(filter(lambda y: y[0] + y[1] >= 5, gen_rndtup(10)), 10)))
    print(sum_ten)
    
print("-----------------------------------------------------")
    
if (__name__=="__main__"):
    
    main()


print("-----------------------------------------------------")

"""
NOTES:
    
    #REDUCE------------------------------------------------------------
    Mfunctools.reduce(function, iterable[, initializer])
    
    Apply function of two arguments cumulatively to the items of 
    iterable, from left to right, so as to reduce the iterable 
    to a single value. 
    
    For example, 
    reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]) 
    calculates ((((1+2)+3)+4)+5).
    
    
    #MAP-------------------------------------------------------------
    map(function, iterable, ...)
    
    Return an iterator that applies function to every item of 
    iterable, yielding the results. If additional iterable arguments 
    are passed, function must take that many arguments and is 
    applied to the items from all iterables in parallel. With 
    multiple iterables, the iterator stops when the shortest 
    iterable is exhausted.
    
    #ISLICE---------------------------------------------------------
    itertools.islice(iterable, stop)
    itertools.islice(iterable, start, stop[, step])
    
    Make an iterator that returns selected elements from the 
    iterable. If start is non-zero, then elements from the 
    iterable are skipped until start is reached. Afterward, 
    elements are returned consecutively unless step is set 
    higher than one which results in items being skipped. 
    If stop is None, then iteration continues until the 
    iterator is exhausted, if at all; otherwise, it stops 
    at the specified position. Unlike regular slicing, 
    islice() does not support negative values for start, 
    stop, or step. Can be used to extract related fields 
    from data where the internal structure has been flattened
    
    #FILTER---------------------------------------------------------
    filter(function, iterable)
    
    Construct an iterator from those elements of iterable for 
    which function returns true. iterable may be either a 
    sequence, a container which supports iteration, or an 
    iterator. If function is None, the identity function 
    is assumed, that is, all elements of iterable that 
    are false are removed.

    Note that filter(function, iterable) is equivalent to 
    the generator expression 
    (item for item in iterable if function(item)) 
    if function is not None and (item for item in iterable if item) 
    if function is None.

    See itertools.filterfalse() for the complementary
    function that returns elements of iterable for which 
    function returns false.
    
"""