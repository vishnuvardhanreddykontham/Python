"""
#1)Write a program to find sum of number.

num = (2,5,8,6)                           
result = sum(num)
print("sum of numbers: ",result)


##output:
sum of numbers:  21





#2)WAP to find the number is strong number or not


sum = 0
num = int(input("please enter number : "))

temp = num
while(num):
    i = 1
    fact = 1 
    rem = num % 10
    while(i<=rem):
        fact = fact*i
        i=i+1
    sum=sum+fact
    num=num//10

if(sum==temp):
      print("Given number is a strong number")  
else:  
    print("Given number is not a strong number")

#outpt:

#please enter number : 145
#Given number is a strong number

#please enter number : 132
#Given number is not a strong number


#3)Python Program to Find the Square Root

num = float(input("enter number: "))
sqrt = num**0.5
print("square root of %0.2f is %0.2f "%(num,sqrt))
            

output:
enter number: 9
square root of 9.00 is 3.00 

enter number: 10
square root of 10.00 is 3.16




#4)Python Program to Calculate the Area of a Triangle


r = float(input("enter the radius : "))
area = 3.14 *r**2
print(area)

#output:
enter the radius : 9
254.34

enter the radius : 5
78.5


##5)Python Program to Solve Quadratic Equation
"""
##first_coefficent = float(input("enter first_coefficent: "))
##second_coefficent = float(input("enter second_coefficent: "))
##constant = float(input("enter constant: "))

##temp = -second_coefficent
##solution_1 = ((second_coefficent**2)-4*(first_coefficent*constant))**0.5
##root_1 = temp + solution_1
##root_2 = temp - solution_1
##
##result = (root_1 + root_2)/(2*first_coefficent)
##print(result)
"""
##output:
##
##enter first_coefficent: 5
##enter second_coefficent: 2
##enter constant: 6
##(-0.4+0j)

##6)Python Program to Swap Two Variables

##first_num = input("enter first number: ")
##second_num = input("enter second number: ")
##
##temp = first_num
##first_num = second_num
##
##second_num = temp
##
##print("value of first_num: ",format(first_num))
##print("value of second_num: ",format(second_num))
##
##output:
##
##enter first number: 45
##enter second number: 60
##value of first_num:  60
##value of second_num:  45

##7)Python Program to Convert Kilometres to Miles


##km = float(input("enter the bike speed in kilometer unit: "))

##conversion_ratio =  0.62137

##miles_1 = km*conversion_ratio

##print("The speed of a bike in miles: ",miles_1)


##output:

##enter the bike speed in kilometer unit: 20
##The speed of a bike in miles:  12.427399999999999

##8)Python Program to Check Leap Year 

##year = int(input("Enter the year: "))

##if(year%4==0 and year%100!=0) or (year%400==0):
##    print(year,"is a leap year")
##else:
##    print(year,"is not a leap year")
##           
##output:

##Enter the year: 2020
##2020 is a leap year

##Enter the year: 2021
##2021 is not a leap year


##9)Python Program to Check Prime Number


##num = int(input("Enter any number: "))
##
##if num>1:
##    for i in range(2,num):
##        if(num%i)==0:
##            print(num,"is not a prime number")
##            break
##    else:
##        print(num,"is a prime number")
            

##else:
##    print(num,"is not a prime number")

##output:

##Enter any number: 13
##13 is a prime number


##10)Python Program to Find the Factorial of a Number

##num = int(input("Enter number: "))
##Factorial = 1
##if num<0:
##    print("Factorial doesnt exist for negative numbers:")
##elif num==0:
##    print("Factorial of 0 is 1: ")
##else:
##    for i in range(1,num+1):
##        Factorial = Factorial*i
##    print("The Factorial of num is", Factorial)


##output:

##Enter number: 10
##The Factorial of num is 3628800

##11)Python Program to Print the Fibonacci sequence

##num = int(input("Enter number: "))
##num_1 = 0
##num_2 = 1
##count  = 0
##
##if num<=0:
##    print("Please enter a positive number,entered number is invalid: ")
##elif num==1:
##    print("Fibonancci sequnce of number up to:",num)
##    print(num_1)
##   
##     
##else:
##    print("The Fibonancci sequnce of number is: ")
##while count<num:
##    print(num_1)
##    nth = num_1+num_2
##    num_1 = num_2
##    num_2 = nth
##      
##    count+=1
##    
##output:
##
##Enter number: 10
##The Fibonancci sequnce of number is: 
##0
##1
##1
##2
##3
##5
##8
##13
##21
##34


#12)Python Program to Check Armstrong Number
  
##num = int(input("Enter number: "))
##sum = 0
##temp = num
##
##while temp>0:
##    digit = temp%10
##    sum += digit**3
##    temp//=10
##if num==sum:
##    print("the entered number is Armstrong number:",num)
##else:
##    print("The entered number is not a Armstrong number:",num)
##
##
##
##output:
##Enter number: 153
##the entered number is Armstrong number: 153
##
##Enter number: 145
##The entered number is not a Armstrong number: 145


##13)Python Program to Find the Sum of Natural Numbers 

num = int(input("Enter number: "))
if num<0:
    print("please enter positive number: ")
else:
    sum = 0
    while(num>0):
        sum+=num
        num-=1
    print("The sum is: ",sum)


output:

Enter number: 6
The sum is:  21


"""

##14)Python Program to Find Armstrong Number in an Interval

##lower_range = int(input("Enter lower range:"))
##upper_range = int(input("Enter upper range:"))
##
##for num in range(lower_range,upper_range + 1):
##
##    sum = 0
##    temp = num
##    while temp>0:
##        digit = temp%10
##        sum += digit**3
##        temp//=10
##        if sum==num:
##            print(sum)
##    
    
##output:
##
##Enter lower range:100
##Enter upper range:1000
##125
##153
##216
##370
##371
##407
##729


##15)Python Program to Find the Factors of a Number


##num = int(input("Enter number: "))
##
##for i in range(1,num+1):
##    if num%i==0:
##        print(i)
##
##output:
##
##Enter number: 90
##1
##2
##3
##5
##6
##9
##10
##15
##18
##30
##45
##90
























    






 

