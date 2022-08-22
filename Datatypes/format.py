"""
print("*****integer*****")
print("{}".format(10))
print("{}{}".format(10,20))
print("{0}".format(10))
print("{0}{1}".format(10,20))
print("{1}{0}".format(10,20))
print("{num1}".format(num1=10))
print("{num1}{num2}".format(num1=10,num2=20))
print("{num2}{num1}".format(num1=10,num2=20))

output:
*****integer*****
10
1020
10
1020
2010
10
1020
2010

print("*****float*****")
print("{}".format(10.11))
print("{}{}".format(10.11,20.22))
print("{0}".format(10.11))
print("{0}{1}".format(10.11,20.22))
print("{1}{0}".format(10.11,20.22))
print("{num1}".format(num1=10.11))
print("{num2}{num1}".format(num1=10.11,num2=20.22))


output:
*****float*****
10.11
10.1120.22
10.11
10.1120.22
20.2210.11
10.11
20.2210.11

print("*****string*****")
print("{}".format("apple"))
print("{},{}".format("apple" , "banana"))
print("{0},{1}".format("apple","banana"))
print("{1},{0}".format("apple","banana"))
print("{st1},{st2}".format(st1="apple",st2="banana"))
print("{st2},{st1}".format(st1="apple",st2="banana"))


output:

*****string*****
apple
apple,banana
apple,banana
banana,apple
apple,banana
banana,apple

print("*****integer and string*****")
print("Hello my name is {}".format("vishnu"))
print("{0}{1}".format(10,"apple"))
print("{1}{0}".format(10,"apple"))
print("{num1},{str1}".format(str1="apple",num1=10))
print("{str1},{num1}".format(str1="apple",num1=10))


output:

*****integer and string*****
Hello my name is vishnu
10apple
apple10
10,apple
apple,10


name = "vishnu"
age = 25
print("my name is {} and my age{}".format(name,age))

output:
    my name is vishnu and my age25

print("Comma as thousand Separator:{:,}".format(1234567890))

output:
Comma as thousand Separator:1,234,567,890

a = 50
b = 3
print("{:2%}".format(a/b))

value = (10,20),(30,40),(50,60)

print("{0[0]},{0[2]}".format(value))

# Format with Dict
data1 ={"rahul":2000,"sonu":3000}
print("{d[rahul]},{d[sonu]}".format(d=data1))

print("{rahul},{sonu}".format(**data1))
"""
print("******** Integer ********")
print("{}".format(15))
print("{:d}".format(15))
print("{0:d}".format(15))






























