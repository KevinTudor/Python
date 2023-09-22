# -*- coding: utf-8 -*-
"""
Spyder Editor

Kevin Tudor

HW 2.1 Problem 1

File Parsing

"""
#Problem 1a: n reads the file indicated by the first parameter and writes its 
#lines prefixed by the line number to the file represented by the second parameter
def line_number(infile, ofile):
    
    #open new output file
    print("Opening new output file:", ofile)
    output_file = open(ofile, "w")
    
    #open input file
    print("Reading file:", infile)
    file_read = open(infile, "r")
    
    #read line-by-line
    x = 0
    for line in file_read:
        
        try:
            print(file_read.tell(), "")   #return cursor position
        except OSError:
            #raise OSError("OSError occured when using .tell()")
            print("OSError occured when using .tell()")
        except:
            raise Exception("Error occured when using .tell()")
            #print("Unknown error occured when using .tell()")
            
        x += 1
        x_str = str(x)
        new_str = x_str + ". " + line
                       
        #write to output file
        output_file.write(new_str) 
        
    output_file.close()
    file_read.close()
        
def parse_functions(infile):

    function = ""
    new_fun = ""
    function_list = []
    fun_list = []
    fun = []
    
    file_read = open(infile, "r")
    
    x = 0
    l = 0
    split = False
    
    for line in file_read:
        x += 1
        fun_name = "" #sum, mul, print_pretty
        f_name = "" #def sum, def mul, def print_pretty
        
        #catch function name
        if(line[0] == "d"):
            for char in line:
                if (char != "("):
                    f_name += char 
                    l += 1
                else:
                    break
            fun_name = (f_name[4:l]) 
        
        
        if (line[0] == "d" or line[0] == "\t"):
            function += line
            
        if (line[1:7] == "return"):
            find = 0
            com_num = 0
            
            for char in function:
                find += 1
                if (char == "#"):
                    split = True
                    com_num = find
                
            find_new = 0
            new_line = []
            for line in function:
                for char in line:
                    find_new += 1
                    if (char == "\n"):
                        new_line.append(find_new)
     
            if (split == True):
                new_fun += function[0:com_num - 2]
                new_fun += function[new_line[0]:len(function)]
                split = False
                
                    
            function_list.append(new_fun)
            new_fun = ""
            function = ""
            
            
        fun = (fun_name, x, function) 
        if (fun[0] != "" and fun[2] != ""):
            fun_list += fun
            
    leng = len(function_list)
    pos = 2
    for z in range(0,leng):
        fun_list[pos] = function_list[z]
        pos += 3
        
    new_list = []     
    for a in range(0, len(fun_list),3):
        new_list.append(fun_list[a])
    new_list.sort()
    
    sort_tuple = ()
    for b in range(0, len(new_list)):
        for a in range(0, len(fun_list),3):
            if (fun_list[a] == new_list[b]):
                sort_tuple += (fun_list[a] , fun_list[a + 1], fun_list[a + 2])
    
    final_tuple = ()
    for a in range(0,len(sort_tuple),3):
        final_tuple += tuple(sort_tuple[a:a+3]),
    
    return final_tuple
    file_read.close()


def main():
    
    open_name = "FileParser/FileParser.py"
    copy_name = "FileParser/Data/Copy.txt"
    line_number(open_name, copy_name)
    
    open_name = "FileParser/Data/File_1.txt"
    print(parse_functions(open_name))
    

print("-----------------------------------------------------")
    
if (__name__=="__main__"):
    main()

print("-----------------------------------------------------")



"""
NOTES:
    
    #Making file object: my_file = open("(filename)", "(mode)")
    #Text file codes: r is read only 
    #[w is write only, a is (append) write at the end of the file, r+ is read and write, w+ is write and read] truncate a file which could erase file when using open function
    #Open file in binary is rb
    
"""




