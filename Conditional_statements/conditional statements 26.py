"""
##1)Print First 10 natural numbers using while loop
num = 0
while num<10:
    num = num+1
    print(num)

output:
1
2
3
4
5
6
7
8
9
10

##2)Calculate the sum of all numbers from 1 to a given number
num = int(input("enter number: "))
sum = 0
for i in range(1,num+1):
    sum += i
    print(sum)
    
output:
enter number: 5
1
3
6
10
15
 
##3)Write a program to print multiplication table of a given number 

num = int(input("Multiplication of given number: "))

for i in range(1,11):
    print(num,'x',i,'=',num*i)

output:

Multiplication of given number: 5
5 x 1 = 5
5 x 2 = 10
5 x 3 = 15
5 x 4 = 20
5 x 5 = 25
5 x 6 = 30
5 x 7 = 35
5 x 8 = 40
5 x 9 = 45
5 x 10 = 50

##4)Display numbers from a list using loop

##list_1 = [1,2,3,4,5,6]
##for i in (list_1):
##    print(i)
##output
##1
##2
##3
##4
##5
##6

##5)count the total number of digits in a number
num = 3654
count = 0

while num!=0:
    num //= 10
    count += 1
print("total number of digits in a number: ",count)
 
output:

total number of digits in a number:  4

##6)Print list in reverse order using a loop

def Reverse(lst):
    new_lst = lst[::-1]
    return new_lst
lst = [10,12,13,14]
print(Reverse(lst))

output:
[14, 13, 12, 10]

#7)numbers from -10 to -1 using for loopDisplay 

ls = []
for i in range(-10,0):

    ls.append(i)
    print(i)

##output:

##-10
##-9
##-8
##-7
##-6
##-5
##-4
##-3
##-2
##-1



##8)Use else block to display a message “Done” after successful execution of for loop

num = 5
for i in range(1,5):
    print(i)
else:
    print("Done")

output:
1
2
3
4
Done


##9)Write a program to display all prime numbers within a range 

lower = 100
upper = 200
print("prime number with in",lower, "and", upper, "are")

for num in range(lower,upper+1):
    if num>1:
        for i in range(2,num):
            if (num%i)==0:
                break
        else:
            print(num)
                
output:

prime number with in 100 and 200 are
101
103
107
109
113
127
131
137
139
149
151
157
163
167
173
179
181
191
193
197
199


##10)Display Fibonacci series up to 10 terms 

nterms = int(input("How many terms? "))


n1, n2 = 0, 1
count = 0


if nterms <= 0:
   print("Please enter a positive integer")

elif nterms == 1:
   print("Fibonacci sequence upto",nterms,":")
   print(n1)

else:
   print("Fibonacci sequence:")
   while count < nterms:
       print(n1)
       nth = n1 + n2
       
       n1 = n2
       n2 = nth
       count += 1

output:

How many terms? 10
Fibonacci sequence:
0
1
1
2
3
5
8
13
21
34

##11)Find the factorial of a given number

num = 10
factorial = 1

for i in range(1,num+1):
    factorial = factorial*i
print("factorial of",num,"is",factorial)

output:

factorial of 10 is 3628800

##12)Reverse a given integer number

num = 1234
reversed_num = 0
while num!=0:
    digit = num % 10
    reversed_num = reversed_num*10 + digit
    num //=10
print("reversed number:",reversed_num)

output:

reversed number: 4321


13)Find the sum of the series upto n terms 

number = int(input('Enter number: '))
print("series_sum= ", number*(number+1)/2) 

#output
Enter number: 10
series_sum=  55.0       

#14)Calculate the cube of all numbers from 1 to a given number 
number = int(input('Enter number: '))
for i in range(1,number+1):
    print(i**3, end=" ")

#output
Enter number: 10
1 8 27 64 125 216 343 512 729 1000

#15)Use a loop to display elements from a given list present at odd index positions 
list1 = list(map(int,input().split()))
i=1
while i<=len(list1)-1:
    if i%2!=0:
        print(list1[i], end=" ")
    i=i+1    

#output
10 20 30 40 50 69
20 40 69    


#16)Name the keyword which helps in writing code involves condition.
if else


#17)Write the syntax of simple if statement. 
if (condition):
    block of code


#18)Is there any limit of statement that can appear under an if block. 
No


#19)Write a program to check whether a person is eligible for voting or not. (accept age from user) 
age = int(input("Enter age")) 

if age>17:
    print("Eligible")
else:
    print("Not Eligible")

#output
Enter age18
Eligible    

#20)Write a program to check whether a number entered by user is even or odd
number = int(input('Enter number: '))

if number%2==0:
    print("Even")
else:
    print("Odd")


#21)a program Write to check whether a number is divisible by 7 or not 
number = int(input('Enter number: '))

if number%7==0:
    print("True")
else:
    print("False")


#22)Write a program to display "Hello" if a number entered by user is a multiple of five , 
# otherwise print "Bye".    
number = int(input('Enter number: '))

if number%5==0:
    print("Hello")
else:
    print("Bye")


#23)Write a program to calculate the electricity bill (accept number of unit from user) according to the following criteria : 

            Unit                                                     Price   

First 100 units                                               no charge 

Next 100 units                                              Rs 5 per unit 

After 200 units                                             Rs 10 per unit  
   

units = int(input('Enter units: '))
if units>0 and units<=100:
    print("no charge")
elif units>=101 and units<=200:
    print('charge=', (units-100)*5)
else:
    print('charge=', 500+(units-200)*10)

#output
Enter units: 20
no charge


Enter units: 150
charge= 250


Enter units: 350
charge= 2000


Enter units: 30
no charge
'''

"""

"""
#24)Write a program to display the last digit of a number. 
number = int(input('Enter number: '))
if number>0:
    print(number%10)

#output
Enter number: 15678
8    

#25)Write a program to check whether the last digit of a number( entered by user ) is  
#divisible by 3 or not. 
number = int(input('Enter number: '))
if number>0:
    rem=number%10
    if rem%3==0:
        print("Last digit divisible by 3")
    else:
        print("no")

#output  
Enter number: 124
no
Enter number: 123
Last digit divisible by 3 
"""

"""
#26)Write a program to accept percentage from the user and display the grade according to the following criteria: 



        Marks                                    Grade 

         > 90                                         A 

         > 80 and <= 90                       B 

        >= 60 and <= 80                       C 

         below 60                                  D        

percentage = int(input("Enter percentage: ")) 
if percentage>90 and percentage<=100:
    print("A")
elif percentage<=90 and percentage>80:
    print("B")
elif percentage<=80 and percentage>=60:
    print("C")
else:
    print("D")

#output 
Enter percentage: 90
B   
Enter percentage: 100
A
"""


"""
#27)Write a program to accept the cost price of a bike and display the road tax to be paid according to the following criteria : 

     

        Cost price (in Rs)                                       Tax 

        > 100000                                                  15 % 

        > 50000 and <= 100000                          10% 

        <= 50000                                                  5% 

cost_price = int(input("Enter cost price: "))
if cost_price>100000:
    print("Road Tax to be paid is Rs.",(15/100)*cost_price)
elif cost_price<=100000 and cost_price>50000:
    print("Road Tax to be paid is Rs.",(10/100)*cost_price)
else:
    print("Road Tax to be paid is Rs.",(5/100)*cost_price)

#output 
Enter cost price: 100001
Road Tax to be paid is Rs. 15000.15  
Enter cost price: 100000
Road Tax to be paid is Rs. 10000.0   



#28)Write a program to check whether an years is leap year or not. 
year = int(input())
if year%4==0:
    if year%100==0:
        if year%400==0:
            print("Leap Year")
        else:
            print("Not a Leap Year")
    else:
        print("Leap Year")
else:
    print("Not a Leap Year")

#output

2000
Leap Year


1900
Not a Leap Year  


##29)Write a program to accept a number from 1 to 7 and display the name of the day like 1 for Sunday , 2 for Monday and so on. 

num = int(input("Enter the number: "))
if num==1:
    print("Sunday")
elif num==2:
    print("Monday")
elif num==3:
    print("Tuesday")
elif num==4:
    print("Wednesday")
elif num==5:
    print("Thuesday")
elif num==6:
    print("Friday")
elif num==7:
    print("Saturday")
else:
    print("Enter valid number")

output:
Enter the number: 9
Enter valid number
Enter the number: 3
Tuesday


##30)Write a program to accept a number from 1 to 12 and display name of the month
##and days in that month like 1 for January and number of days 31 and so on

num = int(input("enter number: "))
dict1 = {1:'January, 31 days', 2: 'February and 28 days', 3: 'March and 31 days', 4: 'April and 30 days',
        5: 'May and 31 days', 6: 'June and 30 days', 7: 'July and 31 days', 8: 'August and 31 days',
        9: 'September and 30 days', 10: 'October and 31 days', 11: 'November and 30 days', 12: 'December and 31 days',
        }
print(dict1[num])

outpu:
enter number: 1
January, 31 days


31)What do you mean by statement? 

Ans:A statement is an instruction that a Python interpreter can execute.

##32)Write the logical expression for the following: 
##
##A is greater than B and C is greater than D
A = 5
B = 3
C = 10
D = 6
if A>B and C>D: 
    print("A is greater than B and C is greater than D")
output:

A is greater than B and C is greater than D


##33)Accept any city from the user and display monument of that city. 
##
##                  City                                 Monument 
##
##                  Delhi                               Red Fort 
##
##                  Agra                                Taj Mahal 
##
##                  Jaipur                              Jal Mahal 

num = int(input("enter number: "))

if num==0:
    print("\tcity\t\t\tMonument")
    
    print("\tDelhi\t\t\tRed Fort")
elif num==1:
    print("\tcity\t\t\tMonument")
    print("\tAgra\t\t\tTaj Mahal")
elif num==2:
    print("\tcity\t\t\tMonument")
    print("\tJaipur\t\t\tJal Mahal")
else:
    print("please enter valid number")

output:

enter number: 2
	city			Monument
	Jaipur			Jal Mahal

34)Write the output of the following if a = 9 

         

    if (a > 5 and a <=10):     

         print("Hello")     

           else:     

        print("Bye") 


a = 10
if (a > 5 and a <=10):
    print("Hello")
else:
    print("Bye")

output:

Hello

##35)Write a program to check whether a number entered is three digit number or not. 
              
num = int(input("Enter number : "))
n = str(num)
if len(n)==4:
    print("entered number is three digit number",num)
    
else:
    print("please enter three digit number")
               
##output:
##Enter number : 456
##entered number is three digit number 456
##Enter number : 4569
##please enter three digit number        


36)Write a program to check whether a person is eligible for voting or not.(voting age >=18) 

age = int(input("Enter candiadte Age : "))
if age<18:
    print("The candidate is not eligible")
else:
    print("The candidate is eligible")
output:
Enter candiadte Age : 10
The candidate is not eligible
    
Enter candiadte Age : 20
The candidate is eligible


#37)Write a program to check whether a person is senior citizen or not

Age = int(input("Please enter Age: "))

if Age>=60:
    print("person is senior citizen:",Age)
else:
    print("person is not a senior citizen:",Age)

output:

Please enter Age: 60
person is senior citizen: 60
Please enter Age: 45
person is not a senior citizen: 45

##38)Write a program to find the lowest number out of two numbers excepted from user.

a = int(input("enter first number: "))
b = int(input("enter second number: "))
if a>b:
    print("lowest number is second")
else:
    print("lowest number is first")

output:

enter first number: 40
enter second number: 30
lowest number is second

enter first number: 30
enter second number: 50
lowest number is first

##39)Write a program to find the largest number out of two numbers excepted from user. 

a = float(input("enter first number: "))
b = float(input("enter second number: "))
if a>b:
    print("largest number is first")
else:
    print("largest number is second")

output:
enter first number: 1.3
enter second number: 2.3
largest number is second

enter first number: 5
enter second number: 3
largest number is first


##40)Write a program to check whether a number (accepted from user) is positive or negative. 
num = int(input("enter number: "))
if num<0:
    print("entered number is negative")
else:
    print("enterd number is positive")
output:
enter number: 10
enterd number is positive
enter number: -10
entered number is negative


##41)Write a program to check whether a number is even or odd. 

num = int(input("enter number: "))
if num%2==0:
    print("entered number is even")
else:
    print("enterd number is odd")
output:
enter number: 15
enterd number is odd

enter number: 20
entered number is even

##42)Write a program to whether a number (accepted from user) is divisible by 2 and 3 both.

num = int(input("enter number: "))
if (num%2==0 and num%3==0):
    print(num,"is divisible by 2 and 3")
else:
    print(num,"is not divisible by 2 and 3")
##output:
##enter number: 3
##3 is not divisible by 2 and 3
##enter number: 12
##12 is divisible by 2 and 3


##43)Write a program to find the largest number out of three numbers excepted from user.

num_1 = int(input("enter first number"))
num_2 = int(input("enter second number"))
num_3 = int(input("enter third number"))

if num_1>num_2 and num_1>num_3:
    print(num_1,"is larger")
elif num_2>num_3:
    print(num_2,"is larger")

else:
    print(num_3,"is larger")

output:

enter first number80
enter second number90
enter third number10
90 is larger


##44)Accept the temperature in degree Celsius of water and check whether it is boiling or not (boiling point of water in 100 oC. 

degree_Celsius = int(input("Enter temperature: "))

if degree_Celsius<100:
    print("water is not boiling")
else:
    print("water is is boiling")

output:
Enter temperature: 70
water is not boiling
                                                                                        
                                                                                         
##45)the age of 4 people and display the youngest one and oldest one? Accept 

age_1 = int(input("enter first person age: "))
age_2 = int(input("enter second person age: "))
age_3 = int(input("enter third person age: "))
age_4 = int(input("enter fourth person age: "))

if age_1>age_2 and age_1>age_3 and age_1>age_4:
    print(age_1,"first person is oldest")
elif age_2>age_3 and age_2>age_4:
    print(age_2,"second person is oldest")
elif age_3>age_4:
    print(age_3,"third person is oldest")
else:
    print(age_4,"fourth person is oldest")

    
if age_1<age_2 and age_1<age_3 and age_1<age_4:
    print(age_1,"first person is youngest")
elif age_2<age_3 and age_2<age_4:
    print(age_2,"second person is youngest")
elif age_3<age_4:
    print(age_3,"third person is youngest")
else:
    print(age_4,"fourth person is youngest")
##outpu:
##enter first person age: 20
##enter second person age: 30
##enter third person age: 40
##enter fourth person age: 50
##50 fourth person is oldest
##20 first person is youngest   

##46)Accept the following from the user and calculate the percentage of class attended: 
##a.     Total number of working days 
##b.     Total number of days for absent 
##After calculating percentage show that, If the percentage is less than 75, than student will not be able to sit in exam. 

working_days = int(input("Enter number of working days: "))
absent_days = int(input("Enter number of absent days: "))

percentage = (absent_days/working_days)*100
print(percentage)

if percentage<75:
    print("student will not be able to sit in exam")
else:
    print("student is eligible to sit in exam")
output:
Enter number of working days: 100
Enter number of absent days: 20
20.0
student will not be able to sit in exam

Enter number of working days: 100
Enter number of absent days: 80
80.0
student is eligible to sit in exam


##47)Accept three sides of a triangle and check whether it is an equilateral, isosceles or scalene triangle. 
##Note : 
##An equilateral triangle is a triangle in which all three sides are equal. 
##A scalene triangle is a triangle that has three unequal sides. 
##An isosceles triangle is a triangle with (at least) two equal sides. 

side_1 = int(input("Enter first side: "))
side_2 = int(input("Enter second side: "))
side_3 = int(input("Enter third side: "))

if side_1==side_2 and side_1==side_3:
    print("is a equilateral triangle")
elif side_1==side_2 or side_1==side_3 or side_2==side_3:
    print("is a isosceles triangle")
else:
    print("is a scalene triangle")
    
##output:
Enter first side: 5
Enter second side: 5
Enter third side: 2
is a isosceles triangle
     

















    

    
    
            

    


    
    





























                                    











    
    
    
