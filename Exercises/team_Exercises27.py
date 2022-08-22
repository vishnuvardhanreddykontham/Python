#================================================================================================== 

#                        Exercise
 #                       --------

#1. Write a program to get all vowels from given string?

##word=input("Enter your word:")
##
##for i in word:
##    print("Result:")
##    if i in ('a','e','i','o','u'):
##        print(i,end=' ')
##    
#output:
#Enter your word: Ramesh
#Result: a e

            
#================================================================================================== 

#2. Write a program to calculate the simple interest?

##prince_amount=int(input("Enter your principle amount:"))
##rate_return=int(input("Enter your rate of return percentage:"))
##time_month=int(input("Enter your time in months:"))
##
##tot=(prince_amount*rate_return*time_month)//100
##print("Simple interest to return: ",tot)
##
##Enter your principle amount:100000
##Enter your rate of return percentage:14
##Enter your time in months:2
##
##Simple interest to return:  28000
#================================================================================================== 

#3. Python Program to Find Sum of Series 1 + 1/2 + 1/3 + 1/4 + ……. + 1/N?

##num=int(input("Enter your number:"))
##s=1
##for i in range(2,num+1):
##    s=s+(1/i)
##print("result:",s)
##
##
##Enter your number:5
##result: 2.283333333333333
##1+1/2+1/3+1/4+1/5
##2.283333333333333
 
#================================================================================================== 

#4. Python Program to Find the Sum of the Series 1/1!+1/2!+1/3!+…1/N!?


##num=int(input("Enter your number:"))
##s=0
##for i in range(1,num+1):
##    fact=1
##    for j in range(1,i+1):
##        fact=fact*j
##    else:
##        s=s+(1/fact)
##print("result:",s)
##
##
##Enter your number:5
##result: 1.7166666666666668
##
###explanation
##1/1 +1/2 +1/6 +1/24 +1/120
##1.7166666666666668
#================================================================================================== 

#5. Python Program to Replace All Occurrences of ‘a’ with $ in a String?


##word=input("enter word:")
##
##for i in word:
##    if i=='a':
##        print('$',end=' ')
##    else:
##        print(i,end=' ')


####enter word:Ramesh
####R $ m e s h
####
####enter word:accomadation
####$ c c o m $ d $ t i o n
#================================================================================================== 

##                    Problem statment
##                    ----------------

""" Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]"""



##nums = [2,7,11,15]
##
##target=9
##
##for i in range(len(nums)-1):
##    for j in range(i+1,len(nums)):
##        if target==(nums[i]+nums[j]):
##            print("indices are:",i,j)
#output:
#indices are: 0 1    


#==================================================================================================

#12.Write a Python program that prints all the numbers from 0 to 6 except 3 and 6. 

"""Note : Use 'continue' statement. 

Expected Output : 0 1 2 4 5  """

##print("Results are:")
##for i in range(0,6+1):
##    if (i==3) or (i==6):
##        continue
##    print(i,end=' ')
##
##
##Results are:
##0 1 2 4 5 
#==================================================================================================

 


   


  












