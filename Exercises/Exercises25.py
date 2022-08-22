##1)WAP for eligibility of a canditate voter_id,
"""
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

2)WAP for calculating student marks in 5-subjects,and find  grades,(suppose grade A,B,C and Fail)?

s1 = int(input("please enter subject-1 marks: "))
s2 = int(input("please enter subject-2 marks: "))
s3 = int(input("please enter subject-3 marks: "))
s4 = int(input("please enter subject-4 marks: "))
s5 = int(input("please enter subject-5 marks: "))
Total = s1+s2+s3+s4+s5

avg = Total//5

if avg<100 and avg>75:
    print("Grade is A:",avg)
elif avg<75 and avg>60:
    print("Grade is B:",avg)
elif avg<60 and avg>40:
    print("Grade is C:",avg)
else:
    print("Fail:",avg)

output:

please enter subject-1 marks: 50
please enter subject-2 marks: 60
please enter subject-3 marks: 50
please enter subject-4 marks: 40
please enter subject-5 marks: 60
Grade is C: 52

3)WAP for finding  even or odd number using (if .. else ... condition)?


num = int(input("Please enter number : "))

if num%2==0:
    print("Entered number is Even")
else:
    print("Entered number is Odd")

outpu:

Please enter number : 15
Entered number is Odd


4)WAP calculating area of a circle, result in positive integers only not in float values

pi = 3.14
radius = int(input("enter the radius: "))
area_of_circle = pi*radius**2
print("area_of_circle is:",int(area_of_circle))

output:

enter the radius: 4
area_of_circle is: 50

"""
##5)WAP for finding  variables A and B are having the same memory location?

##var_1 = int(input("Enter first value : "))
##var_2 = int(input("Enter second value : "))
##
##if var_1==var_2:
##    print("variable are having same memory locations")
##
##else:
####    print("variable are not having same memory locations")

##output:
##Enter first value : 50
##Enter second value : 60
##variable are not having same memory locations


##Enter first value : 50
##Enter second value : 50
##variable are having same memory locations
##
##
##                      problem statement:

##n = int(input("Enter range of a number: "))
##l = []
##for i in range(n):
##    ip = int(input("enter values:"))
##    l.append(ip**2)
##for i in l:
##    print(i)
##
##output:
##
##Enter range of a number: 4
##enter values:5
##enter values:6
##enter values:4
##enter values:3
##25
##36
##16
##9
    














    
