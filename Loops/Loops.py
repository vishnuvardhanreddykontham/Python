"""
##1)Accept 10 numbers from the user and display their average.

num = 10
sum = 0
for i in range(1,num+1):
    sum = sum + i
##print(sum)
avg = sum/i
print("The average of",num,"is",avg)

##output:
##The average of 10 is 5.5

##2)Write a program to display sum of odd numbers and even numbers that fall between 12 and 37(including both numbers)
sum_1 = 0
sum_2 = 0
for i in range(12,37):
    if i%2==0:
        sum_1 = sum_1+i
    else:
        sum_2 = sum_2+i
print("value of sum_1",sum_1)
print("value of sum_2",sum_2)
    
output:

value of sum_1 312
value of sum_2 288

##3)Write a program to display all the numbers which are divisible by 11 but not by 2 between 100 and 500. 

for i in range(100,500):
    if i%11==0 and i%2==1:
        print(i)
output:
121
143
165
187
209
231
253
275
297
319
341
363
385
407
429
451
473
495

##4)Write a program to print numbers from 1 to 20 except multiple of 2 & 3 

for i in range(1,20):
    
    if i%2==0 or i%3==0:
        pass
    else:
        print(i)
        
output:
1
5
7
11
13
17
19

##5)Write a program that keep on accepting number from the user until user enters Zero.
##Display the sum and average of all the numbers. 
sum = 0
count = 0
while True:

    num = int(input("enter number: "))
    if num==0:
        break
    else:
        count = count+1
        sum = sum+num
print(sum,sum/count)
    
output:
enter number: 15
enter number: 20
enter number: 25
enter number: 30
enter number: 0
90 22.5

##6)Write a program to accept decimal number and display its binary number.
 
def decimalToBinary(n): 
    return bin(n).replace("0b","") 
 
if __name__ == '__main__': 
    print(decimalToBinary(8)) 
    print(decimalToBinary(18)) 
    print(decimalToBinary(7))

output:
1000
10010
111


##7)Convert the following loop into for loop : 
##
##x = 4 
##
##while(x<=8): 
##
##    print(x*10) 
##
##    x+=2

x = 4
for x in range(x,8,2):
    print(x*10)
   
8)What is nested loop? 
Ans:A nested loop is a loop inside the body of the outer loop. The inner or outer loop can be any type,
such as a while loop or for loop. For example, the outer for loop can contain a while loop and vice versa.


##9)Write a program to convert temperature in Fahrenheit to Celsius
Fahrenheit = float(input("enter temperature in fahrenheit: "))

celsius = (Fahrenheit-32)/1.8

print(celsius)

output:
enter temperature in fahrenheit: 100
37.77777777777778

##10)Write a Python program to get the Fibonacci series between 0 to 50.  


num_1 = 1
num_2 = 1
print(num_1,end=" ")
print(num_2,end=" ")
while True:
    
    nth = num_1+num_2
    if nth>=50:
        break
        
    print(nth,end=" ")
        
    
    num_1 = num_2
    num_2 = nth

##output:
##0, 1, 1, 2, 3, 5, 8, 13, 21, .... 
##
##Every next number is found by adding up the two numbers before it. 
##
##Expected Output : 1 1 2 3 5 8 13 21 34 
##1 1 2 3 5 8 13 21 34 
 

##11)Write a Python program which iterates the integers from 1 to 50.
##For multiples of three print "Fizz" instead of the number and for the multiples of five print "Buzz".
##For numbers which are multiples of both three and five print "Fizz Buzz". 
##
##Sample Output : 
##
##fizzbuzz 
##
##1 
##
##2 
##
##fizz 
##
##4 
##
##Buzz        

for num in range(1,50):
    if (num%3==0 and num%5==0):
        print("Fizz Buzz")
        
    elif num%3==0:
        print("Fizz")
    elif num%5==0:
        print("Buzz")
    else:
        print(num)

output:

1
2
Fizz
4
Buzz
Fizz
7
8
Fizz
Buzz
11
Fizz
13
14
Fizz Buzz
16
17
Fizz
19
Buzz
Fizz
22
23
Fizz
Buzz
26
Fizz
28
29
Fizz Buzz
31
32
Fizz
34
Buzz
Fizz
37
38
Fizz
Buzz
41
Fizz
43
44
Fizz Buzz
46
47
Fizz
49

##12)Write a Python program that prints all the numbers from 0 to 6 except 3 and 6. 
##
##Note : Use 'continue' statement. 
##
##Expected Output : 0 1 2 4 5

for i in range(0,6):

    if i%3==0 or i%6==0:
        continue
    print(i)

output:
1
2
4
5

"""





























