                   Exercises
##1)WAP to reverse a number

num = int(input("enter any number: "))
print(str(num)[::-1])
output:
enter any number: 321
123

##2)WAP to count  the number  occurrence/frequency  of a  each character in a string .

string = input("enter string: ")
char = input("enter your charecter: ")
count = 0

for i in range(len(string)):
    if (string[i]==char):
        count = count+1
print("Total number of times",char,"occured in string=",count)
output:
enter string: vikatakavi
enter your charecter: a
Total number of times a occured in string= 3

##3)WAP  to check length of two string is equal or not.

string_1 = input("enter string_1: ")
string_2 = input("enter string_2: ")
if len(string_1)==len(string_2):
    print("length of two string is equal")
else:
    print("length of two string is not equal")
output:
enter string_1: vishnu
enter string_2: vardhan
length of two string is not equal

##4)Python program to print even numbers up to 100

for i in range(0,101):
    if i%2==0:
        print(i)
output:
0
2
4
6
8
10
12
14
16
18
20
22
24
26
28
30
32
34
36
38
40
42
44
46
48
50
52
54
56
58
60
62
64
66
68
70
72
74
76
78
80
82
84
86
88
90
92
94
96
98
100
"""
