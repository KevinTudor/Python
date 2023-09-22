# -*- coding: utf-8 -*-
"""
Problem 3.1

Vector/class
"""
import numpy as np

#use CamelCase NO UNDERLINE
class NVector(object):  #represent N-dimensional vector of real-numbers

    #constructor
    def __init__(self, *seq): 
        self.new_lst = []
        
        if (len(seq) == 1):
            #print("len() of sequence: ", len(seq))
            self.new_lst += seq[0]
        else:
            #print("length of vector sequence: ", len(seq))
            self.vector = np.array(seq)
            
    #find length of vector       
    def __len__(self):
        if (self.new_lst):   
            return len(self.new_lst)
        else:  
            return len(self.vector)
        
    #return element at given index   
    def __getitem__(self, index):
        if (self.new_lst):   
            return self.new_lst[index]
        else:  
            return self.vector[index]
    
    #set item at index to value
    def __setitem__(self, index, value):
        if (index < len(self.new_lst)):
            if (self.new_lst): 
                self.new_lst[index] = value
            else:  
                self.vector[index] = value
        else:
            raise IndexError('index larger than length of list by: ', index - len(self.new_lst))
    
    #return the string representation of the NVector object
    def __str__(self):
        if (self.new_lst): 
            return 'List object is : {}' .format(str(self.new_lst))
        else:
            return 'Vector is : {}' .format(str(self.vector))
    
    #take a parameter and return true if self is equal(respectively) to parameter obj
    def __eq__(self, v2):
        if (self.new_lst and v2.new_lst):  
            if (self.new_lst == v2.new_lst):
                return True
            else:
                return False
        else:
            eq_fl = True
            if (len(self) == len(v2)):
                for x in range(0,len(v2)):
                    if (self[x] != v2[x]):
                        eq_fl = False
                return eq_fl        
            else:
                return False
            
    def __ne__(self, v2):
        if (self.new_lst and v2.new_lst):  
            if (self.new_lst != v2.new_lst):
                return True #not equal
            else:
                return False #equal
        else:
            eq_fl = False #assume equal
            if (len(self) == len(v2)): #if same length
                for x in range(0,len(v2)):
                    if (self[x] != v2[x]):
                        eq_fl = True #not equal
                return eq_fl        
            else: #if not same length
                return True #not equal
            
    def __add__(self, param1):
        #print("in add")
        add_lst = []
            
        if(isinstance(param1, int)):
            for x in range(0,len(self.new_lst)):
                add_lst.append(self.new_lst[x] + param1)
        else:
            if (len(self.new_lst) < len(param1.new_lst)):
                s = len(self.new_lst)
                l = len(param1.new_lst)
            else:
                s = len(param1.new_lst)
                l = len(self.new_lst)
            
            for x in range(0,s):
                add_lst.append(self.new_lst[x] + param1.new_lst[x])
                
            if (len(self.new_lst) > len(param1.new_lst)):
                for x in range(s,l):
                    add_lst.append(self.new_lst[x])
                
            if (len(self.new_lst) < len(param1.new_lst)):
                for x in range(s,l):
                    add_lst.append(param1.new_lst[x])
            
        return (NVector(add_lst))
            
    def __radd__(self, param1):
        #print("in radd")
        add_lst = []
        
        if(isinstance(param1, int)):
            for x in range(0,len(self.new_lst)):
                add_lst.append(self.new_lst[x] + param1)
        
        return (NVector(add_lst))
    
    def __mul__(self, param1):
        #print("\nin mul")
        mul_lst = []
        result = 0
        
        if(isinstance(param1, int)):
            for x in range(0,len(self.new_lst)):
                mul_lst.append(self.new_lst[x] * param1)
        else:
            
            if (len(self.new_lst) < len(param1.new_lst)):
                s = len(self.new_lst)
                l = len(param1.new_lst)
            else:
                s = len(param1.new_lst)
                l = len(self.new_lst)
            
            for x in range(0,s):
                mul_lst.append(self.new_lst[x] * param1.new_lst[x])
                
            if (len(self.new_lst) > len(param1.new_lst)):
                for x in range(s,l):
                    mul_lst.append(self.new_lst[x])
                
            if (len(self.new_lst) < len(param1.new_lst)):
                for x in range(s,l):
                    mul_lst.append(param1.new_lst[x])
                    
        #print(mul_lst)            
        for x in range(0, len(mul_lst)):
            result += mul_lst[x]
   
        return (result)
    
    def __rmul__(self, param1):
        #print("\nin rmul")
        mul_lst = []
        result = 0
        
        if(isinstance(param1, int)):
            for x in range(0,len(self.new_lst)):
                mul_lst.append(self.new_lst[x] * param1)
           
        for x in range(0, len(mul_lst)):
            result += mul_lst[x]
   
        return (result)
    
    def zeros(n):
        z_lst = []

        for x in range(0,n):
            z_lst.append(0)
            
        return (NVector(z_lst))


#(k) testif
def testif(b, msgOK="", msgFailed=""):
    if b:        
        print("Success: " + msgOK)
    else:
        print("Failed: "+ msgFailed)
        
    return b
    
def main():
        
    n1 = NVector([3,0,1,-1])
    print("(a1)Testing constructor with 1 list obj\nResult:", n1)
    testif(isinstance(n1, NVector),"Constructor initilized list as new list obj", "Failed")
    
    n2 = NVector((3,0,1))
    print("\n(a2)Testing constructor with 1 tuple obj\nResult:", n2)
    testif(isinstance(n2, NVector),"Constructor initilized tuple as new list obj", "Failed")
    
    n3 = NVector(3,0,1,-1)
    print("\n(b)Testing constructor with two or more arguments\nResult:", n3)
    testif(isinstance(n3, NVector),"Constructor initilized two or more arguments as new vector", "Failed")
    
    print("\n(c)Testing method __len__\nResult:", n1.__len__())
    testif(n1.__len__() == 4,"method __len__ == 4", "Failed")
    
    print("\n(d1)Testing method __getitem__(index)\nResult:", n1[1])
    testif(n1[1] == 0,"method __getitem__(1) == 0", "Failed")
    
    print("\n(d2)Testing method __getitem__(-index)\nResult:", n1[-2])
    testif(n1[-2] == 1,"method __getitem__(-2) == 1", "Failed")
    
    n1[3] = 10
    print("\n(e1)Testing method __setitem__(index, value)\nResult:", n1)
    testif(n1[3] == 10,"method __setitem__(3,10) == [3, 0, 1, 10]", "Failed")
    
    n2[-1] = 30
    print("\n(e2)Testing method __setitem__(-index, value)\nResult:", n2)
    testif(n2[-1] == 30,"method __setitem__(-1,30) == [3, 0, 30]", "Failed")
    
    print("\n(f)Testing method __str__\nResult:", n1.__str__())
    testif(isinstance(n1.__str__(), str),"n1.__str__ is type string", "Failed")
    
    n4 = NVector([3,0,1,1])
    n5 = NVector([3,0,1,1])
    print("\n(g1)Testing method __eq__ (true equal)\nResult:", n4.__eq__(n5))
    testif(n4.__eq__(n5) == True,"method __eq__ if equal return True", "Failed")
    
    print("\n(g2)Testing method __eq__ (false equal)\nResult:", n1.__eq__(n5))
    testif(n1.__eq__(n5) == False,"method __eq__ if not equal return False", "Failed")
    
    print("\n(g3)Testing method __ne__ (true  not equal)\nResult:", n1.__ne__(n5))
    testif(n2.__ne__(n5) == True,"method __ne__ if not equal return True", "Failed")
    
    print("\n(g4)Testing method __eq__ (false equal)\nResult:", n4.__ne__(n5))
    testif(n4.__ne__(n5) == False,"method __eq__ if equal return False", "Failed")
    
    ans = NVector([6, 0, 31, 10])
    print("\n(h1)Testing method __add__ (n1 + n2)", "\nV1:", n1, "\nV2:", n2, "\nResult:", n1 + n2)
    testif(n1 + n2 == ans,"method __add__ (n1 + n2 == ans)", "Failed")
    
    ans = NVector([5, 2, 3, 12])
    print("\n(h2)Testing method __add__ (n1 + int)", "\nV1:", n1, "\nint:", 2, "\nResult:", n1 + 2)
    testif(n1 + 2 == ans,"method __add__ (n1 + int == ans)", "Failed")
    
    print("\n(h3)Testing method __add__ (int + n1)", "\nint:", 2, "\nV1:", n1, "\nResult:", n1 + 2)
    testif(2 + n1 == ans,"method __add__ (int + n1 == ans)", "Failed")
    
    ans = 49              #NVector = ([9, 0, 1, 10])
    print("\n(i1)Testing method __mul__ (n1 * n2)", "\nV1:", n1, "\nV2:", n2, "\nResult:", n1 * n2)
    testif(n1 * n2 == ans,"method __mul__ (n1 * n2 == ans)", "Failed")
    
    ans = 28              #NVector = ([6, 0, 2, 20])
    print("\n(i2)Testing method __mul__ (n1 * int)", "\nV1:", n1, "\nint:", 2, "\nResult:", n1 * 2)
    testif(n1 * 2 == ans,"method __add__ (n1 * 2 == ans)", "Failed")
    
    print("\n(i3)Testing method __mul__ (int * n1)", "\nint:", 2, "\nV1:", n1, "\nResult:", 2 * n1)
    testif(2 * n1 == ans,"method __add__ (n1 * 2 == ans)", "Failed")
    
    ans = NVector([0, 0, 0, 0, 0])  # not required
    print("\n(j)Testing method zeros(n)", "\nn:", 5, "\nResult:", NVector.zeros(5))
    testif(NVector.zeros(5) == ans,"method zeros(n) == ans", "Failed")
    
    n1[3] = 10  #change index to 30
    print("\n(e1)Testing method __setitem__(index, value) **EXCEPTION**\n")
    testif(n1[3] == 10,"no exception thrown", "Failed")
    
print("-----------------------------------------------------")
 
if (__name__=="__main__"):
    main()
    
print("-----------------------------------------------------")


"""
NOTES:
    
**private attributes**
    --------------------------
    __name -> Class__name
    
    
**Function call**
    --------------------------
    do_something(param1)
    
    
**method call**
    --------------------------
    an_object.do_something(param1)
    
    object the method is called on 
    is always implicitly a parameter
    

**return print instead of reference location**
    ---------------------------
    
    def __str__(self):
        return (self.attr1)
    
    def __repr__(self):
        return (self.__str__())


"""