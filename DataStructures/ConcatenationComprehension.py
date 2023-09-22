# -*- coding: utf-8 -*-
"""
Spyder Editor

Kevin Tudor

HW 2.2 Problem 2

Concatenation/Comprehension

"""

def part_a(): 
    
    lst = [(a,b,c) for a in range(1,101) for b in range(1,101) for c in range(b,101) if a**2 + b**2 == c**2]

    return (lst)

def part_b():
    
    test1 =  ['one', 'seven', 'three', 'two', 'ten']    
    lst = []
    
    #not comprehension
    for element in test1:
        if (len(element) > 3):
            lst.append(tuple((len(test1),element.upper())))

    #comprehension    
    lst = [(len(test1),element.upper()) for element in test1 if len(element) > 3 ]
        
    return lst
    
def part_c():
    
    test1 =  ["Jules Verne", "Alexandre Dumas", "Maurice Druon"]     
    
    #not comprehension
    lst = []
    for element in test1:
        for x in range(1,len(element)):
            if (element[x] == " "):
                lst += (element[x+1:len(element)],element[0:x])
       
    #comprehension
    lst = [element[x+1:len(element)]+", "+element[0:x] for element in test1 for x in range(1,len(element)) if (element[x] == " ")]
    return (lst)

def concatenate(s, a, b, c) :
    
    new_str = a + (s + b if b != '' else '') + (s + c if c != '' else '')
    
    return (new_str)

def main():
    
    print(part_a())
    print()
    print(part_b())
    print()
    print(part_c())
    print()
    print(concatenate(": ", "one", "two", "three"))
    print(concatenate(' and ', "Bonny", "Clyde", ""))
    print(concatenate(' and ', "single", "", "")) 
    

print("-----------------------------------------------------")
    
if (__name__=="__main__"):
    main()

print("-----------------------------------------------------")

