# Classification-Using-Python-and-Regex
**Problem Statement:**

Consider you have given two set of data points in the form of list of tuples like 
Red =[(R11,R12),(R21,R22),(R31,R32),(R41,R42),(R51,R52),..,(Rn1,Rn2)] 

Blue=[(B11,B12),(B21,B22),(B31,B32),(B41,B42),(B51,B52),..,(Bm1,Bm2)] and set of line equations(in the string formate, i.e list of strings) 

Lines = [a1x+b1y+c1,a2x+b2y+c2,a3x+b3y+c3,a4x+b4y+c4,..,K lines] Note: you need to string parsing here and get the coefficients of x,y and intercept your task is to for each line that is given print "YES"/"NO

You will print yes, if all the red points are one side of the line and blue points are other side of the line, otherwise no Ex: 

Red= [(1,1),(2,1),(4,2),(2,4), (-1,4)] 

Blue= [(-2,-1),(-1,-2),(-3,-2),(-3,-1),(1,-3)] 

Lines=["1x+1y+0","1x-1y+0","1x+0y-3","0x+1y-0.5"]
