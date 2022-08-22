                                     problem statement by team-3
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
  

