"""
##1. How would you confirm that 2 strings have the same identity?

s1 = input("Enter string1: ")
s2 = input("Enter string2: ")
print(id(s1))
print(id(s2))
if len(s1)==1 and len(s2)==1:
    if id(s1)==id(s2):
        print("Two strings have same identity")
    else:
        print("Two strings have different identity")
else:
    print("Two strings have different identity")

output:
Enter string1: vishnu
Enter string2: vardhan
2578920781744
2578914684336
Two strings have different identity


##2. How would you check if each word in a string begins with a capital letter?

st = input("VishnuVardhanReddy")

st.istitle()
print(" is capital letter:",st.istitle())


#3. Check if a string contains a specific substrin
st = "plane"
st1 = "The worlds fastest plane"
if st in st1:
    print("yes plane in The worlds fastest plane")
else:
    print("no plane is not in The worlds fastest plane")
output:
yes plane in The worlds fastest plane

#4)Find the index of the first occurrence of a substring in a string

st = "vishnu vardhan reddy".index('reddy')
st = "vishnu vardhan reddy".find('reddy')
print("index of reddy is:", st)

output:

index of reddy is: 15


##5) Count the total number of characters in a string

st = "vishnuvardhanreddy"
result = len(st)
print("Length of a",st,"is:" ,result)

output:

Length of a vishnuvardhanreddy is: 18

##6)Count the number of a specific character in a string

st = "vishnuvardhanreddy".count('v')
print("v in: ",st)


##output:
##v in: 2

##7)Capitalize the first character of a string

st = "vishnuvardhanreddy".capitalize()
print(st)

output:

Vishnuvardhanreddy

#8)What is an f-string and how do you use it?
name = "vishnuvardhan reddy"
age = 25
print("my name is {},and my age is {}".format(name,age))

output:
my name is vishnuvardhan reddy,and my age is 25

##9. Search a specific part of a string for a substring
st = "vishnuvardhanreddy".index('reddy',1,20)
print("reddy",st)

output:

reddy 13

#10) Interpolate a variable into a string using format()

thing = "exam"
difficulty = "easy"
print("the {} is very {}".format(thing,difficulty))

output:

the exam is very easy

#11)Check if a string contains only numbers

st = '1000'
if st.isnumeric():
    print("yes")
else:
    print("no")

output:
yes

#12)Split a string on a specific character

st = "this is a python code".split()
print(st)
output:

['this', 'is', 'a', 'python', 'code']

#13)Check if a string is composed of all lower case characters

st = "Python is language"
if st.islower():
    print("yes")
else:
    print("no")

output:
yes

#14)Can an integer be added to a string in Python?

st = "pyhton" + 10
print(st)

output:
st = "pyhton" + 10
TypeError: can only concatenate str (not "int") to str

#15)Check if the first character in a string is lowercase

st = 'pYTHON'
if st[0].islower():
    print("yes")
else:
    print("no")
output:
yes

#16)Reverse the string “hello world”
st = "hello world"[::-1]
print(st)
output:
dlrow olleh

#17) Join a list of strings into a single string, delimited by hyphens
st = 'python is a string'
temp=st.replace(' ','-')
print(temp)

output:

python-is-a-string


#18)Check if all characters in a string conform to ASCI

print( 'Â'.isascii() )
print( 'A'.isascii() )
output:
False
True


#19)Uppercase or lowercase an entire string
st = input("enter string: ")
if st.isupper():
    print(st,"is a uppercase")
else:
    print(st,"is a lowercase")
    
output:
enter string: VISHNU
VISHNU is a uppercase

#20)Uppercase first and last character of a string
lang = 'python'
result = lang[0].upper() + lang[1:-1] + lang[-1].upper()
print(result)

output:

PythoN

#21)Check if a string is all uppercase

st = input("enter string: ")
if st.isupper():
    print(st,"yes")
else:
    print(st,"no")

output:

enter string: vishnu
vishnu no

#22)When would you use splitlines()?

sentence = "python \nis a \nlanguage"
result=sentence.splitlines()
print(result)

output:
['python ', 'is a ', 'language']

#23)Give an example of string slicing

string = 'I like to eat apples'
result = string[:6]
print(result)
result1=string[7:13]
print(result1)
result2=string[0:-1:2]
print(result2)

output:
I like
to eat
Ilk oetape

#24)Convert an integer to a string

st = "20"
print(type(st))
output:
<class 'str'>

#25)Check if a string contains only characters of the alphabet

st = "1pyhton"
result = st.isalpha()
print(result)

output:
True

#26)Replace all instances of a substring in a string

st = "python is a good language python is easy"
result=st.replace("python","java")
print(result)

output:
java is a good language java is easy


#27)Return the minimum character in a string

st = "java"
result = min(st)
print(result)

output:
a

#28)Check if all characters in a string are alphanumeric

st = "python3"
result = st.isalnum()
print(result)

##output:
##True

#29)Remove whitespace from the left, right or both sides of a string

st="    python    "
print(st.lstrip())
print(st.rstrip())
print(st.strip())


output:  
python    
    python
python

"""

#30)Check if a string begins with or ends with a specific character

st = "python"
result = st.startswith("p")
print(result)
result1 = st.startswith("o")
print(result1)

output:
#True
False
























