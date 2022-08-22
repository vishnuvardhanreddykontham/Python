"""
#1.Take 10 integer inputs from user and store them in a list and print them on screen.
a =[1,2,3,4,5,6,7,8,9,10]
b = []
for i in range(1,11):
    c = int(i)
    b.append(c)
print(b)
#output:[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#2.Take 10 integer inputs from user and store them in a list. Again ask user to give a number. Now, tell user whether that number is present in list or not.
#( Iterate over list using while loop ).
i=1
lst=[]
while i<=10:
        a=int(input('Enter any number: '))
        i=i+1
        lst.append(a)
print(lst)
b=int(input('Enter any number: '))
if b in lst:
    print('Number in list')
else:
    print('Not in list')

#3.Take 20 integer inputs from user and print the following:
#number of positive numbers
#number of negative numbers
#number of odd numbers
#number of even numbers
#number of 0s.
a =[3,4,6,7,-9,-8,2,12,14,-3,12,16,18,19,21,22,24,23,26,27]
negitivecount = 0
positivecount = 0
evencount = 0
oddcount = 0
zero = 0
for i in a:
    if(i<0):
        negitivecount = negitivecount+1
for i in a:
    if(i>0):
        positivecount = positivecount+1
for i in a:
    if(i%2==0):
        evencount = evencount+1
for i in a:
    if(i%2!=0):
        oddcount = oddcount+1
for i in a:
    if(i==0):
        zero = zero+1
print("negitive: ",negitivecount,"positive: ",positivecount,"evencount: ",evencount,"oddcount: ",oddcount,"zero: ",zero)
#output:negitive:  3 positive:  17 evencount:  12 oddcount:  8 zero:  0 '''   
#4.Take 10 integer inputs from user and store them in a list. Now, copy all the elements in another list but in reverse order.
a = int(input("enter the number: "))
b =[]
for i in range(1,a+1):
    c = int(i)
    b.append(c)
print(b)
print(b[::-1])
#output:enter the number: 10
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
####[10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
#5.Write a program to find the sum of all elements of a list.
a = [1,5,8,5]
sum = 0
for i in a:
    sum = sum+i
print(sum)
output:19
#6.Write a program to find the product of all elements of a list.
a = [1,2,3,4,5]
product = 1
for i in a:
    product = product * i
print(product)
#output:120
#7.Initialize and print each element in new line of a list inside list.
a = [1,2,3,4,5,6]
b = str(a)
c = b.split(',')
for i in c:
    print(i,"\n")
#[1 

 2 

 3 

 4 

 5 

 6]
#8.Find largest and smallest elements of a list.
a =[1,2,3,4,5]
print("min: ",min(a))
print("max: ",max(a))
#output:min:  1
max:  5
#9.Write a program to print sum, average of all numbers, smallest and largest element of a list.
a = [1,2,3,4,5]
sum = 0
avg = 0
print("min: ",min(a))
print("max: ",max(a))
for i in a:
    sum = sum +i
    avg = sum/5
print("sum: ",sum)
print("avg: ",avg)
output:min:  1
max:  5
sum:  15
avg:  3.0
#10.Write a program to check if elements of a list are same or not it read from front or back. E.g.-
#2   3  15  15	3	2

a = [2,3,15,15,3,2]
rev = a[::-1]
if(a == rev):
    print("same")
else:
    print("not same")
#output:same
#11.Take a list of 10 elements. Split it into middle and store the elements in two dfferent lists. E.g.-
#INITIAL list :
#58	24	13	15	63	9	8	81	1	78
a = [58,24,13,15,63,9,8,81,1,78]
b = a[:5]
c =a[5:]
print(b)
print(c)
#output:[58, 24, 13, 15, 63]
[9, 8, 81, 1, 78]
"""
#12.Ask user to give integer inputs to make a list. Store only even values given and print the list.
a = int(input("enter the value: "))
b=[]
for i in range(1,a+1):
    if(i%2==0):
        b.append(i)
print(b)
#enter the value: 20
#[2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

    
    
