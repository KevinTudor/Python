
# -*- coding: utf-8 -*-
"""
Spyder Editor

Kevin Tudor

HW 2.3 Problem 3

contact list/ csv

"""

import csv

def part_a(c_l, na,ni,p):

    empty = True
    
    for x in range(0,len(c_l),3):
        #if in list
        if(c_l[x][0] == na):
            #change to new entry, return false
            c_l.pop(x)
            c_l.append(tuple((na,ni,p)))
            empty = False
        #else, return true
        else:
            c_l.append(tuple((na,ni,p)))
            empty = True
            
    #if list empty add new     
    if(len(c_l) == 0):
        c_l.append(tuple((na,ni,p)))
        empty = True
        
    #sort alphabetically    
    c_l.sort()
            
    print(c_l) 
       
    return empty

def part_b(c_l, na,ni,p):
    
    for x in range(0,len(c_l)):
        #if in list
        if(c_l[x][0] == na):
            #remove entry, return true
            c_l.pop(x)
            print(c_l)
            return True
    
    print(c_l)
            
    return False
    
def part_c(c_l, na,ni):
    
    for x in range(0,len(c_l)):
        #if in list
        if(c_l[x][0] == na or c_l[x][1] == ni):
            #remove entry, return true
            return c_l[x]
            
def part_d(c_l,f_name):
    
    csv_file = open(f_name, "w")
    
    write = csv.writer(csv_file)
    
    title = ["Name: ","Nickname: ","Phone Number: "]
    
    write.writerow(title)
    write.writerows(c_l)
    
    csv_file.close()
      
def part_e(f_name):
    
    csv_file = open(f_name, "r")
    
    lst = []
    
    for line in csv_file:
        if (line[0:4] != "Name" and line[0] != '\n'):
            lst.append((line[0:len(line)-1]))
            
    #lst2 = [(line[0:len(line)-1]) for line in csv_file if line[0:4] != "Name" and line[0] != '\n']
            
    csv_file.close()
            
    return lst

def main():
    #create list
    c_l = []
    
    #add contact to list/replace existing and sort alphabetically
    print("Add contacts\n")
    
    print(part_a(c_l, "Earl Simmons", "DMX", "305-1010101"))
    print()
    print(part_a(c_l, "Cardi B", "Belcalis", "305-4399521"))
    print()
    print(part_a(c_l, "Beyonce Knowles", "bey", "561-4444444"))
    print()
    print(part_a(c_l, "Beyonce Knowles", "bey", "561-1234321"))
    print()

    #remove contact from list is exists
    print("remove contacts\n")
    
    #print(part_b(c_l, "Beyonce Knowles", "bey", "561-1234321"))
    #print()
    print(part_b(c_l, "Cardi B", "Belcalis", "305-4399521"))
    print()
    
    #find contact by name or nickname if exists
    print("find contacts\n")
    print(part_c(c_l, "", "beey"))
    print()
    print(part_c(c_l, "Earl Simmons", "DMX"))
    print()
    
    #save list to .csv file
    print("save contact list\n")
    part_d(c_l, "FileParser/Data/csv_file.csv")
    
    #read and return contact list object
    print("read and return contact list\n")
    print(part_e("FileParser/Data/csv_file.csv"))

print("-----------------------------------------------------")
    
if (__name__=="__main__"):
    main()

print("-----------------------------------------------------")

