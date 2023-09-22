# -*- coding: utf-8 -*-
"""
Spyder Editor

Kevin Tudor

Homework 4 (file manipulation)

Problem 1

file editor
"""
import os.path


""" ed_read docstring part a 

return as a string the content of the file named filename,
with file positions in the half-open range [from, to). If to == -1, the content between from and
the end of the file will be returned. If parameter to exceeds the file length, then the function
raises exception IndexError with a corresponding error message. 

"""
def ed_read(filename, fro = 0, to = -1):
    
    temp = ""
    temp_str = ""
    
    #copy file to string
    with open(filename, "r") as open_f: # open/close
        file_lst = open_f.readlines()
    for element in file_lst:
        temp_str += element 
        
    #create new string of given indeces to return    
    if (to == -1):
        with open(filename, "r") as open_f: # open/close
            open_f.seek(fro)       # start at from location
            temp += open_f.read(1) # read first char
            temp += open_f.read()  # read to EOF
            
    elif (to > len(temp_str)):
        raise IndexError("Index " + str(to) + " out of range of file size")
        
    else:
        with open(filename, "r") as open_f: #open file, close file when suite ends
            open_f.seek(fro)       # start at from location
            temp += open_f.read(1) # read first char
            temp += open_f.read(to - fro - 1)  # read remaining char excluding index to (9)
            
    return temp

""" ed_find docstring part a

finds string search_str in the file named by filename and returns
a list with index positions in the file text where the string search_str is located. E.g. it returns
[4, 100] if the string was found at positions 4 and 100. It returns [] if the string was not found.
 
"""
def ed_find(filename, search_str):
    
    find_index = []
    file_lst = []
    temp_str = ""
    
    with open(filename, "r") as open_f: # open/close
        file_lst = open_f.readlines()
    #print(file_lst)
    
    for element in file_lst:
        temp_str += element  
    #print(temp_str)
    
    for x in range(0, len(temp_str)):
        if (temp_str[x:x + len(search_str)] == search_str):
            find_index.append(x)       
    #print(find_index) 
       
    return find_index


""" ed_replace docstring part a 

replaces search_str in the file
named by filename with string replace_with. If occurrence==-1, then it replaces ALL
occurrences. If occurrence>=0, then it replaces only the occurrence with index occurrence,
where 0 means the first, 1 means the second, etc. If the occurrence argument exceeds the actual
occurrence index in the file of that string, the function does not do the replacement. The
function returns the number of times the string was replaced. 

"""
def ed_replace(filename, search_str, replace_with, occurrence=-1):
    
    file_lst = []
    temp_str = ""
    new_temp = ""
    
    #find the occurences of search_str
    lst = ed_find(filename, search_str)
    
    #copy file to string
    with open(filename, "r") as open_f: # open/close
        file_lst = open_f.readlines()
    
    for element in file_lst:
        temp_str += element 
        
    #print(temp_str)
    
    #replace occurance of search_str to replace_with
    if (occurrence == -1):
        new_temp = temp_str.replace(search_str,replace_with)
        #print(new_temp)
        
    if (occurrence >= 0 and occurrence < len(lst)):
        temp1 = temp_str[0:lst[occurrence]]
        temp2 = temp_str[lst[occurrence] + len(search_str):]
        new_temp = temp1 + replace_with + temp2
        #print(new_temp)
    
    if (occurrence >= len(lst)):
        new_temp = temp_str
    
    #re-write new string with replacment to truncated file
    with open(filename, "w") as open_f: # truncate then open/close
        open_f.write(new_temp)
    
    #find # of times the replaced word in in the new file then return value
    lst2 = ed_find(filename, replace_with)
    
    #print(len(lst2))
    return len(lst2)


""" ed_append docstring part a

appends string to the end of the file. If the file does not exist, a
new file is created with the given file name. The function returns the number of characters
written to the file. 
 
"""
def ed_append(filename, string):
    
    #print("Opening file:", filename)
    if (os.path.isfile(filename) == False ): # if cant open said file
        with open(filename, "w") as open_f: #open new write file
            open_f.write(string)         #write to file
    else:
        with open(filename, "a") as open_f: #open append file
            open_f.write(string)
     
    return len(string)     #return the number of characters written to file   
   

""" testif docstring #part b

Write test functions for functions ed_replace and ed_find using the testif() function we used for
homework 3, listed in Appendix A. These test functions should be named test_x , where x is the name
of the function tested. E.g. test_ed_write() should use testif() to test ed_write(). In general, this type of
test functions are called unit tests as they test just one function (or one method in a class).  
 
"""
def testif(b, testname, msgOK="", msgFailed=""):
 
   if b: 
       print("Success: "+ testname + "; " + msgOK) 
   else:    
       print("Failed: "+ testname + "; " + msgFailed) 
   return b

# testif ed_replace module
def test_ed_replace():
    
    #set up the file
    fn = "FileParser/Data/file_tst_rep.txt" # assume this file does not exist yet.
    
    if os.path.exists(fn):  # if file already exists
        os.remove(fn)       #remove file to reset it
        
    ed_append(fn, "0123456789") # this will create a new file
    ed_append(fn, "0123456789") # the file content is: 01234567890123456789
    
    testif(ed_replace(fn, "345", "ABCDE") == 2, "test_ed_replace", "replaced 2x", "Fail" )

# testif ed_replace module
def test_ed_find():
    
    #set up the file
    fn = "FileParser/Data/file_tst_find.txt" # assume this file does not exist yet.
    
    if os.path.exists(fn):  # if file already exists
        os.remove(fn)       #remove file to reset it
        
    ed_append(fn, "0123456789") # this will create a new file
    ed_append(fn, "0123456789") # the file content is: 01234567890123456789
    
    testif(ed_find(fn, "345") == [3,13], "test_ed_find", "found 2x", "Fail" )


#part c
def main():
    fn = "FileParser/Data/file1.txt" # assume this file does not exist yet.
    
    if os.path.exists(fn):  # if file already exists
        os.remove(fn)       #remove file to reset it
        
    ed_append(fn, "0123456789") # this will create a new file
    ed_append(fn, "0123456789") # the file content is: 01234567890123456789
    
    print(ed_read(fn, 3, 9)) # prints 345678. Notice that the interval excludes index to (9)
    print(ed_read(fn, 3)) # prints from 3 to (-1) the end of the file: 34567890123456789
    #print(ed_read(fn, 3, 900)) # raises index error
    
    lst = ed_find(fn, "345")
    print(lst) # prints [3, 13]
    print(ed_find(fn, "356")) # prints []
    #ed_replace(fn, "345", "ABCDE", 0) # changes the file to 012ABCDE67890123456789
    #ed_replace(fn, "345", "ABCDE", 1) # changes the file to 0123456789012ABCDE6789
    #ed_replace(fn, "345", "ABCDE", 2)  # occurrence 2 DNE so do nothing
    # assume we reset the file content to 01234567890123456789 (not shown)
    #ed_replace(fn, "345", "ABCDE") # changes the file to 012ABCDE6789012ABCDE6789


print("-----------------------------------------------------")
    
if (__name__=="__main__"):
    main()
    test_ed_replace()
    test_ed_find()

print("-----------------------------------------------------")


"""
NOTES:
    
    #Making file object: my_file = open("(filename)", "(mode)")
    #Text file codes: r is read only 
    #[w is write only, a is (append) write at the end of the file, r+ is read and write, w+ is write and read] truncate a file which could erase file when using open function
    #Open file in binary is rb
    
"""