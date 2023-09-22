# -*- coding: utf-8 -*-
"""
Spyder Editor

Kevin Tudor

HW1.1 Problem 1

Quadratic Equations:

Write a program with a loop that :
a) solves quadratic equations with coefficients read from the terminal,
b) visualizes the corresponding quadratic function y=ax^2+bx+c using the 
   matplotlib.pyplot module 
(replacing module pylab used in the book)

"""
import math
import matplotlib.pyplot as graph

num_root = 0

while True:

    a_str = input("Enter (valid float number) value for coefficient a:  ")
    if(a_str == ''):
        break
    a = float(a_str)
    
    b_str = input("Enter (valid float number) value for coefficient b:  ")
    b = float(b_str)
    
    c_str = input("Enter (valid float number) value for coefficient c:  ")
    c = float(c_str)
    
    y = (b * b)-(4 * a * c)
    
    if (y < 0): #3, 0, 1
        print("No real solutions")
        num_root = 0
        
    elif (y == 0): #1, 2, 1
        x1 = (-b) / (2 * a)
        print("One solution: ", x1)
        num_root = 1
        
    else: #1, -1, -6
        x1 = (((-b) - math.sqrt(y)) / (2 * a))
        x2 = (((-b) + math.sqrt(y)) / (2 * a))
        print("Two solutions: ", x1, " ", x2)
        num_root = 2
        
    #---------------------GRAPH-----------------------------------------------    

    xs = []
    ys = []
    
    # prepare the domain for the function we graph
    if (num_root == 0):
        # center function domain (x values) on the function’s minimum or maximum value
        center = (-b) / (2 * a)   # center
        lb = center - 2           # lower bound
        ub = center + 2           # upper bound
       
    elif(num_root == 1):
        lb = x1 - 2    # lower bound
        ub = x1 + 2    # upper bound
        
    else:
        lb = x1 - 2    # lower bound
        ub = x2 + 2    # upper bound
    
    # prepare # of points
    n = 150                    # n points (150)
    dx = (ub - lb) / (n - 1)   # delta between points (dx = 1)
    
    # center the graph
    x = lb         # center
    
    #populate the list
    while x <= ub: 
        xs.append(x) # add element at the end of the list xs(push back)
        
        # edit this function
        y = (a * (x * x)) + (b * x) + c
        
        ys.append(y) # add element at the end of the list ys(push back)
        x += dx # increment x not total of n points
        
    # after the loop:
    graph.plot(xs, ys, "r")    # creates the graph figure, but does not show it yet
    graph.title("Quadratic Equations")        # title
    graph.xlabel("x")           # x label
    graph.ylabel("y")           # y label
    
    
    if(num_root == 1):         # plot points if one root
        y = (a * (x1 * x1)) + (b * x1) + c
        graph.plot(x1, y, "ro-")
    elif(num_root == 2):       # plot points if two roots
        y1 = (a * (x1 * x1)) + (b * x1) + c
        graph.plot(x1, y1, "ro-")
        y2 = (a * (x2 * x2)) + (b * x2) + c
        graph.plot(x2, y2, "ro-")
       
    graph.show()                # Show the graph
    
print("\nEND OF PROGRAM")

