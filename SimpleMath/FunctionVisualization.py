# -*- coding: utf-8 -*-
"""
Spyder Editor

Kevin Tudor

HW1.1 Problem 4

Function Visualization:

"""

import math # compiler says not used for function eval on line 42
import matplotlib.pyplot as graph

def plot_function(fun_str, domain, samples):
    
    # initialize the lists
    xs = []
    ys = []
    table = []
    
    # prepare the domain for the function we graph
    lb = domain[0]
    ub = domain[1] 
    
    # prepare # of points
    dx = (ub - lb) / (samples - 1)   # delta between points (dx = 1)
    
    # starting (left) value
    x = lb         
    
    #populate xs
    while x <= ub: 
        xs.append(x) #add element at the end of the list (push back)
        x += dx
    
    #populate ys
    for x in xs:
        y = eval(fun_str)
        ys.append(y)
        # populate values for table using tuples
        table.append(tuple([x, y]))
        
    # after the loop: fill out plot
    graph.plot(xs, ys, "ro-")   # creates the graph figure, doesn't show yet
    graph.title(fun_str)        # title
    graph.xlabel("x")           # x label
    graph.ylabel("y")           # y label
    graph.show()                # show plot
    
    # print the table using format
    print("____________________")
    print('{:>5s}{:>10s}'.format('x','y'))
    print("____________________\n") 
    
    for i in range (0, samples):
        print(' {:>+5.4f} {:>+9.4f}'.format(table[i][0],table[i][1]))
        
    print("____________________")

while True:
    
    fun_str = input("Enter function with variable x: ")
    
    if(fun_str == ''):
        break
    
    num_sam = input("Enter number of samples: ")
    
    sam = int(num_sam)
    
    if(sam <= 0):
        print("Invalid number of samples")
        break
    
    samples = int(num_sam)
    
    x_min_in = input("Enter xmin: ")
    
    x_min = int(x_min_in)
    
    x_max_in = input("Enter xmax: ")
    
    x_max = int(x_max_in)
    
    domain = tuple([x_min, x_max])
    
    plot_function(fun_str, domain, samples)
    
    
    
    
    
    


    