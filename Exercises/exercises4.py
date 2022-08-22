#1.write a python program to print the pattern
h = eval(input("Enter diamond's height: "))
for x in range(h):
    print(" " * (h - x), "*" * (2*x + 1))
for x in range(h - 2, -1, -1):
    print(" " * (h - x), "*" * (2*x + 1))
output:
Enter diamond's height: 5
      *
     ***
    *****
   *******
  *********
   *******
    *****
     ***
      *

#2.How would you check if each word in a string begins with a capital letter?
by using method title()

#3.Write a Python program that prints all the numbers from 0 to 6 except 4 and 5.
for i in range(0,7):
    if i==4 or i==5:
        continue
    else:
        print(i)

output:

0
1
2
3
6


#4.Print list of elements and store in a another list and print  reverse order of list 
ls=[1,2,3,4]
ls1=ls.copy()
print(ls1)
print(ls1[::-1])
output:

[1, 2, 3, 4]
[4, 3, 2, 1]

#Pattern
print("Print equilateral triangle Pyramid with characters ")
size = 7
asciiNumber = 65
m = (2 * size) - 2
for i in range(0, size):
    for j in range(0, m):
        print(end=" ")
    m = m - 1
    for j in range(0, i + 1):
        character = chr(asciiNumber)
        print(character, end=' ')
        asciiNumber += 1
    print(" ")


Print equilateral triangle Pyramid with characters 
            A  
           B C  
          D E F  
         G H I J  
        K L M N O  
       P Q R S T U  
      V W X Y Z [ \  

















