#                                                   5-Exercises by team-2
#==========================================================================================================================================

##Q1.WAP in python arrange string characters such that lowercase letters should come first


##char=input("enter your sentence:")
##low=[]
##high=[]
##for i in char:
##    for j in range(65,91+1):
##        if i==chr(j):
##            high.append(i)
##            break
##    else:
##        low.append(i)
##
##print("Upper Case: ")
##for i in high:
##    if i==' ':
##        continue
##    print(i,end=' ')
##
##print()
##print("lower case:")
##for j in low:
##    if j==' ':
##        continue
##    print(j,end=' ')
##
##
##enter your sentence:Ramesh is in On the FOrth Bench in the GARDEN
##Upper Case: 
##R O F O B G A R D E N 
##lower case:
##a m e s h i s i n n t h e r t h e n c h i n t h e 

#==========================================================================================================================================

##Q2.WAP to print sum of prime numbers in given list input :- 2 4 5 6 7 3 8 output :- 17


##lst=[int(x) for x in input("Enter your numbers with comma(,) separation:").split(',')]
##s=0
##for i in lst:
##    for j in range(2,i):
##        if i%j==0:
##            break
##    else:
##        s=s+i
##print("sum of prime numbers:",s)

##Enter your numbers with comma(,) separation:2,4,5,7,6,3,8
##sum of prime numbers: 17

##Enter your numbers with comma(,) separation:2,3,4,5,6,7,8,9,10,11,12,13,14,17,19,21,27,31,37,39,29
##sum of prime numbers: 174
#==========================================================================================================================================

##Q3.when do we use nested for loop.Write an example?

#=> nested for loop:

##*loop means, it is an iterative or traversing throughout the collection or sequentional datatype.
##
##* nested loop is nothing, but "loop in the loop" till the given problem statement gets satisfy.



#example:

##lst=[int(x) for x in input("Enter your numbers with comma(,) separation:").split(',')]
##s=0
##for i in lst:
##    for j in range(2,i):
##        if i%j==0:
##            break
##    else:
##        s=s+i
##print("sum of prime numbers:",s)
#==========================================================================================================================================

##Q4.WAP in python remove all characters from a string except integers(ex:- STR="H56U1E9JIG3l4w2" ,o/p:-5619342(only display integers) )


##char=input("enter your sentence:")
##for i in char:
##    if i.isdigit():
##        print(i,end=' ')
##
##enter your sentence:gfjgh43578438
##4 3 5 7 8 4 3 8
#==========================================================================================================================================

##Q5.WAP to take a list and find the possition of the item .(eg=  [45,12,66,2,33] if i take 66 then it shows the index 2)?


##lst=[int(x) for x in input("Enter your numbers with comma(,) separation:").split(',')]
##
##t=int(input("enter your trigared point:"))
##
##for i in lst:
##    if t==i:
##        print("Index is :",lst.index(i))
##
##
##Enter your numbers with comma(,) separation:25,4,2,3,6
##enter your trigared point:2
##Index is : 2
#==========================================================================================================================================

#                                   problem statement by team-3
#                                   ---------------------------


#==========================================================================================================================================
"""
Python Program to accept three distinct digits and print all possible combinations from the digits.

Case 1:

Enter first number:1
Enter second number:2
Enter third number:3
                    1 2 3
                    1 3 2
                    2 1 3
                    2 3 1
                    3 1 2
                    3 2 1

Case 2:

Enter first number:5
Enter second number:7
Enter third number:3
                    5 7 3
                    5 3 7
                    7 5 3
                    7 3 5
                    3 5 7
                    3 7 5      """



num=int(input("enter any number:"))

l=[]
for i in range(1,num+1):
    ip=input("enter your {} number:".format(i))
    l.append(ip)

for i in range(num):
    print(l[i],end=' ')
    for j in range(i+1,num):
        print(l[j],end=' ')
    print()
  



#==========================================================================================================================================


