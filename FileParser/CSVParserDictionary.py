# -*- coding: utf-8 -*-
"""
Spyder Editor

Kevin Tudor

HW 2.4 Problem 4

CSV files and dictionaries using data from IMDB lists 

#search if title, director, actor1 are in top rated list 
#if in top rated list count amount of movies 
#the director and actor made together 
#(director, actor1, movies made together and in rated list)

"""

def display_top_collaborations():
    open_cast = open("FileParser/Data/imdb-top-casts.CSV", "r", encoding = 'utf-8')
    open_rate = open("FileParser/Data/imdb-top-rated.CSV", "r", encoding = 'utf-8')

    movie_tuple = ()
    movie_dic = {'title': '', 'director': '', 'actor1': ''}
    
    #find the movie title, director and actor 1 in top cast
    for line in open_cast:
        cast_line = tuple(line.split(","))
        movie_tuple = (cast_line[0], cast_line[2], cast_line[3])
        movie_dic[cast_line[0]] = cast_line[2], cast_line[3]
       
    movie_title = []
    #find the movie title in top rated
    for line in open_rate:
        cast_line = tuple(line.split(","))
        movie_tuple = (cast_line[1])
        movie_title.append(movie_tuple)
    
    #find movies in both
    title_list = []
    for key in movie_dic:
        for title in movie_title:
            if (key == title):
                title_list.append(movie_dic[key])
                
    #add num movies together to tuple
    final_list = []
    for element in title_list:
        num = 0
        for x in title_list:
            if (element == x):
                num += 1
        final_list.append((element, num))
    
    #sort by decending
    final_list.sort(key=lambda y:y[1], reverse=True)
    
    #error checking
    dupe = False
    i = 0
    for a in final_list:
        for b in final_list:
            if (a == b and dupe == False):
                dupe = True
            elif(a == b and dupe == True):
                final_list.remove(a)
            i += 1  
    
    for x in range(0,5):
        print(final_list[x])         
        
    open_cast.close()
    open_rate.close()
    
def display_top_directors():
    
    open_gross = open("FileParser/Data/imdb-top-grossing.CSV", "r", encoding = 'utf-8')
    open_cast = open("FileParser/Data/imdb-top-casts.CSV", "r", encoding = 'utf-8')

    gross_tuple = ()
    gross_list = []
    movie_dic = {'title': '', 'director': ''}  
        
    #find list of lop grossing movie
    for line in open_gross:
        gross_line = tuple(line.split(","))
        gross_tuple = (gross_line[1], gross_line[3][0:len(gross_line[3])-1])
        gross_list.append(gross_tuple)
    
    #print(gross_list)
    
    
    #find the movie title and director in top cast
    for line in open_cast:
            cast_line = tuple(line.split(","))
            movie_tuple = (cast_line[0], cast_line[2], cast_line[3])
            movie_dic[cast_line[0]] = cast_line[2]
            
    #print(movie_dic)
    
    #find director and money for movie
    dir_mon = ()
    gross_movie = []
    for element in gross_list:
        for key in movie_dic:
            if(element[0] == key):
                dir_mon = (movie_dic[key],element[1])
                gross_movie.append(dir_mon)
                
    #print(gross_movie)
    
    #find total money each actor
    dir_mon = ()
    mon_list = []
    for element in gross_movie:
        money = 0
        for director in gross_movie:
            if(element[0] == director[0]):
                money += int(director[1])
        dir_mon = (element[0], money)
        mon_list.append(dir_mon)
                       
    #print(mon_list)
    
    mon_list.sort(key = lambda y: y[1], reverse = True)
    
    
    #error checking
    dupe = False
    for a in mon_list:
        for b in mon_list:
            if (a == b and dupe == False):
                dupe = True
            elif(a == b and dupe == True):
                mon_list.remove(a)   
                
    final_list = []         
    for x in range(0,20): 
        if (mon_list[x] == mon_list[x+1]):
            final_list.append(mon_list[x])
            mon_list.remove(mon_list[x+1])
        else:
            mon_list.append(mon_list[x])
            
    #end error checking        
    for x in range(0,5):
        print(mon_list[x])
        
        
    open_cast.close()
    open_gross.close()
    
    
def main():
    print("Top 5 collaborations: ")
    display_top_collaborations() 
    print("\nTop 5 total grossing directors: ")
    display_top_directors()
    

print("-----------------------------------------------------")
    
if (__name__=="__main__"):
    main()

print("-----------------------------------------------------")

