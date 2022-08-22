#                                   5-Exercises
#                                   -----------
"""

#============================================================================================================================================

#1. WAP to find the target value of 5 in the given list of 1,5,7,8,90,6,and 23 elements?

target = 5
list = [1,5,7,8,90,6,23]
print(list)
print("The index of target is:",list.index(target))
##output:
[1, 5, 7, 8, 90, 6, 23]
The index of target is: 1


#============================================================================================================================================

#2. WAP to sort the given list of elements 1,5,7,8,90,6,and 23, without using sort() function?

list = [1,5,7,8,90,6,23]
for i in range(len(list)):
    for j in range(i+1,len(list)):
        if list[i]>list[j]:
            list[i],list[j]=list[j],list[i]
print("sorted elements:",list)

output:
sorted elements: [1, 5, 6, 7, 8, 23, 90]


#============================================================================================================================================

#3. WAP to calcalte the compound interest of 3 years with the priciple amount of RS:10000 and rate of return is 5 percentage for annum.
#  and display the total amount to pay on  the end of the year.?
"""
principle = int(input("enter amount:"))
rate = int(input("enter rate:"))
time = int(input("enter time:"))
compound_intrest =principle*(1+rate/100)**time

print("compound intrest is:",compound_intrest)

Total_amount = compound_intrest+principle
print("Total amount is:",Total_amount)

##output:
enter amount:10000
enter rate:5
enter time:3
compound intrest is: 11576.250000000002
Total amount is: 21576.25
"""

#==========================================================================================================================================

#4. WAP to calculate the sum of the given matrix   [[x1,x2,x3],[x4,x5,x6],[x7,x8,x9]], where x1,x2....x9 values must take from command-line
#   arguments?
""" #1 2 3
##    4 5 6  
##    7 8 9   
##
##sum is : 45   """
"""
l = []
for i in range(1,10):
    value = int(input("Enter {} element:".format(i)))
    l.append(value)

sum = 0
for i in l:
    sum = sum+i
          
print(sum)

output:

Enter 1 element:3
Enter 2 element:5
Enter 3 element:6
Enter 4 element:4
Enter 5 element:5
Enter 6 element:6
Enter 7 element:1
Enter 8 element:8
Enter 9 element:9
47
"""
#=============================================================================================================================================

#5. WAP pattern program

"""  * * * * *
      * * * *
       * * *
        * *
         *
        * *
       * * *
      * * * * 
     * * * * *     """

##
##rows = 5
##
##k = (2*rows)-2
##
##for i in range(rows, -1, -1):
##    for j in range(k, 0, -1):
##        print(end=" ")
##k = k + 1
##for j in range(0, i + 1):
##    print("*", end=" ")
##
##    print("")
##



















