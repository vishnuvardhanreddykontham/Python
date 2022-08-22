
#                   pattern Questins
#                   ----------------

#1. Write a program to print the following Patterns
"""
  1 2 3 4 5 
  1 2 3 4 5  
  1 2 3 4 5 
  1 2 3 4 5 
  1 2 3 4 5"""


##for i in range(1,5+1):
##    for j in range(1,5+1):
##        print(j,end=' ')
##    print()


#==================================================================================================

#2.Write a program to print the following Pattern
"""
  5 4 3 2 1 
  5 4 3 2 1
  5 4 3 2 1
  5 4 3 2 1
  5 4 3 2 1"""



##for i in range(1,5+1):
##    for j in range(5,0,-1):
##        print(j,end=' ')
##    print()

#==================================================================================================

#3.Write a program to print the following Pattern
"""
  5 5 5 5 5 
  4 4 4 4 4 
  3 3 3 3 3 
  2 2 2 2 2 
  1 1 1 1 1"""



##for i in range(5,0,-1):
##    for j in range(1,5+1):
##        print(i,end=' ')
##    print()



#==================================================================================================

#4.Write a program to print the following Pattern
"""
  1
  1 2
  1 2 3
  1 2 3 4
  1 2 3 4 5"""



##for i in range(1,5+1):
##    for j in range(1,i+1):
##        print(j,end=' ')
##    print()


#==================================================================================================

#5.Write a program to print the following Pattern
"""
  1 
  2 2 
  3 3 3 
  4 4 4 4 
  5 5 5 5 5"""


##for i in range(1,5+1):
##    for j in range(1,i+1):
##        print(i,end=' ')
##    print()

#==================================================================================================

#6.Write a program to print the following Pattern
"""
  1 
  2 3  
  4 5 6 
  7 8 9 10 
  11 12 13 14 15"""


##t=1
##for i in range(1,5+1):
##    for j in range(1,i+1):
##        print(t,end=' ')
##        t=t+1
##    print()


#==================================================================================================


#7.Write a program to print the following Pattern
"""
  5 
  4 4 
  3 3 3 
  2 2 2 2 
  1 1 1 1 1"""

##n=5
##for i in range(1,5+1):
##    for j in range(1,i+1):
##        print(n,end=' ')
##    n=n-1    
##    print()



#==================================================================================================

#8.Write a program to print the following Pattern
"""
  1 
  2 3 
  3 4 5 
  4 5 6 7 
  5 6 7 8 9"""


##for i in range(1,5+1):
##    for j in range(1,i+1):
##        print(i,end=' ')
##        i=i+1  
##    print()

#==================================================================================================

#9.Write a program to print the following Pattern
"""
  A 
  B C
  D E F
  G H I J
  K L M N O"""


##t=65
##for i in range(65,69+1):
##    for j in range(65,i+1):
##        print(chr(t),end=' ')
##        t=t+1
##    print()




#10.Write a program to print the following Pattern
"""
   * * * * * 
   * * * * * 
   * * * * * 
   * * * * * 
   * * * * *"""


##for i in range(1,5+1):
##    for j in range(1,5+1):
##        print('*',end=' ')
##    print()


#==================================================================================================

#11.Write a program to print the following Pattern
"""
   * 
   * * 
   * * * 
   * * * * 
   * * * * *   """


##for i in range(1,5+1):
##    for j in range(1,i+1):
##        print('*',end=' ')
##    print()

#==================================================================================================

#12.Write a program to print the following Pattern
""" * * * * * 
    *       * 
    *       * 
    *       * 
    * * * * *  """

##for i in range(0,5):
##    for j in range(0,5):
##        if  (i==4)or (j==4) or (i==0) or (j==0):
##            print('*',end='  ')
##        else:
##            print('  ',end=' ')
##    print()

#==================================================================================================

#13.Write a program to print the following Pattern
"""       * 
        * * * 
      * * * * * 
    * * * * * * *  """
##a=1
##for i in range(5,0,-1):
##    print(' '*i,end='')
##    for j in range(1,5+1):
##        print("* "*a,end=' ')
##        a=a+1
##        break
##    print()

#==================================================================================================

#14.Display Multiplication Table in given range using Nested for loops


##for i in range(1,5+1):
##    for j in range(1,10+1):
##        print(i,"*",j,"=",i*j)
##    print()

#==================================================================================================

#15.Display Prime Numbers in the given range using nested for loops 

##for i in range(2,100):
##    for j in range(2,i):
##        if i%j==0:
##            break
##    else:
##        print(i,end=' ')
#2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97 
#==================================================================================================

#16.Write a program to print the following Pattern

""" 

                 1
              3  2
         6   5   4
     10  9   8   7
t=1
s=3

for i in range(1,5):
    print(' '*s**2,end=' ')
    l=[]
    for j in range(1,i+1):
        #print(t,end=' ')
        l.append(t)
        t=t+1
    for i in range(len(l)-1,-1,-1):
        print(l[i],end=" ")
        
    s=s-1
    
    print() 
"""




"""
t=1
s=3
for i in range(1,5):
    print(' '*s*2,end=' ')
    for j in range(i,0,-1):
        print(t,end=' ')
        t=t+1
    s=s-1
    
    print()


       1 
     2 3 
   4 5 6 
 7 8 9 10   """



#==================================================================================================

#17.Write a program to print the following Pattern

"""10  9  8   7
       6   5  4
           3  2
              1 """


##t=10
##s=0
##for i in range(4,0,-1):
##    print(' '*s**2,end=' ')
##    for j in range(1,i+1):
##        print(t,end=' ')
##        t-=1
##    s=s+1
##    print()


"""
t=10
s=0
for i in range(4,0,-1):
    print(' '*s,end=' ')
    for j in range(1,i+1):
        print(t,end=' ')
        t-=1
    s=s+1
    print()




10 9 8 7 
 6 5 4 
  3 2 
   1  """







#==================================================================================================
"""""
A
B D
C F I
D H L P
E J O T Y
F L R X
G N U
H P
I

        """

##
##t=1
##a=65
##for i in range(1,5+1):
##    for k in range(1,6):
##        pass
##    for j in range(1,i+1):
##        print(chr(a),end=' ')
##        
##
##    a=a+1
##    print()
        
