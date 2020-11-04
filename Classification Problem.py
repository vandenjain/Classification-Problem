#!/usr/bin/env python
# coding: utf-8

# # Problem Statement

# Consider you have given two set of data points in the form of list of tuples like 
# Red =[(R11,R12),(R21,R22),(R31,R32),(R41,R42),(R51,R52),..,(Rn1,Rn2)] 
# Blue=[(B11,B12),(B21,B22),(B31,B32),(B41,B42),(B51,B52),..,(Bm1,Bm2)] and set of line equations(in the string formate, i.e list of strings) 
# Lines = [a1x+b1y+c1,a2x+b2y+c2,a3x+b3y+c3,a4x+b4y+c4,..,K lines] Note: you need to string parsing here and get the coefficients of x,y and intercept your task is to for each line that is given print "YES"/"NO
# 
# You will print yes, if all the red points are one side of the line and blue points are other side of the line, otherwise no Ex:
# 
# Red= [(1,1),(2,1),(4,2),(2,4), (-1,4)] 
# 
# Blue= [(-2,-1),(-1,-2),(-3,-2),(-3,-1),(1,-3)] 
# 
# Lines=["1x+1y+0","1x-1y+0","1x+0y-3","0x+1y-0.5"]

# In[1]:


import math
import re
# Defining the test cases
Red= [(1,1),(2,1),(4,2),(2,4), (-1,4)]
Blue= [(-2,-1),(-1,-2),(-3,-2),(-3,-1),(1,-3)]
Lines=["1x+1y+0","1x-1y+0","1x+0y-3","0x+1y-0.5"]

initial_red = []
initial_blue= []
final_red = []
final_blue = []

#Splitting the coefficients of x,y and intercept from line equation
for line in Lines:
    p, q, r = [float(ite.strip()) for ite in re.split('x|y', line)]
    Red_ = []
    Blue_= []
    
    #For Red points
    for i in range(len(Red)):
        m = ((p*Red[i][0]) + (q*Red[i][1]) + r)
        Red_.append(m)
    initial_red.append(Red_)
    
    #For Blue points
    for j in range(len(Blue)):
        n = ((p*Blue[j][0])+ (q*Blue[j][1])+ r)
        Blue_.append(n)
    initial_blue.append(Blue_)
    
#Checking the position of red and blue points w.r.t. line
final_red = ([all(k > 0 for k in i) for i in initial_red] or [all(k < 0 for k in i) for i in initial_red])
final_blue = ([all(j < 0 for j in i) for i in initial_blue] or [all(j > 0 for j in i) for i in initial_blue])

#Checking if the red and blue points are on the same side of the line or not
for i in range(len(final_blue)):
    if(final_blue[i] == True and final_red[i] == True):
        print("YES")
    else:
        print("NO")    


# In[ ]:




