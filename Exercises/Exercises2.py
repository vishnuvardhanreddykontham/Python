"""
1)Calculate income tax for the given income by adhering to the below rules
Taxable Income    Rate (in %)
First $10,000    0
Next $10,000    10
The remaining    20
Expected Output:

For example, suppose the taxable income is 45000 the income tax payable is

10000*0% + 10000*10%  + 25000*20% = $6000.


income = int(input("Enter income: "))

if income>=0 and income<=10000:
    print("income tax for the",income,"is",0)

elif income>=10000 and income<=20000:
     (r==income-10000)
     print("income tax for the",income,"is",(10/100)*r)
   
    
    
elif 20000<=income and income<=45000:
    print("income tax for the",income,"is",(20/100)*income)

##2.Count the length of list with out using any inbuilt function.

##
##l = [int(x) for x in input().split()]
##c=0
##for i in l:
##    c=c+1
##print("length:",c)
"""
t= input("enter word: ")
l = list(t)

c=0
for i in l:
    c =c+1
print("length:",c)

"""
##4. Take input from user and if input is string print String
##if input is integer/float print integer
##if input is mix of string and integer print Error
##HINT Can be done using ASCII code

value = str(input("Enter value:"))

if int(value):
    print(value)
elif float(value):
    
    print(value)
elif str(value):
    print(value)
else:
    print("error")



#5.Python program to check if a string is palindrome or not

s = input("Enter string: ")
t=""
for i in (s[::-1]):
    t = t+i
if s==t:
    print("is a palindrom")
else:
    print("is not a palindrom")
    
"""



























































