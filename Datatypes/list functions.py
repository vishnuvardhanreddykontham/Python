"""
A = [1,2,3,4,"hi","pyhton",10.25]
print(A)
#result = A.index(10.25)
result = A.index("pyhton")
print(result)



# Append() - To enter a new value at the end of the list.

A = [1,2,3,4,"hi","pyhton",10.25]
A.append(6)
print(A)
A.append(8)
print(A)

##output:
[1, 2, 3, 4, 'hi', 'pyhton', 10.25, 6]
[1, 2, 3, 4, 'hi', 'pyhton', 10.25, 6, 8]

# Insert() - To insert a new value at a given index in the list.

A = [1,2,3,4,"hi","pyhton"]
A.insert(2,10)
print(A)

A.insert(5,"Language")
print(A)
A.index("Language")
print(A.index("Language"))

####output:
[1, 2, 10, 3, 4, 'hi', 'pyhton']
[1, 2, 10, 3, 4, 'Language', 'hi', 'pyhton']
5




# Remove() - To delete a value from the list.


A = [1, 2, 10, 3, 4, 'Language', 'hi', 'pyhton']

A.remove("Language")
print(A)

A[5] = "JAVA"
print(A)

output:
[1, 2, 10, 3, 4, 'hi', 'pyhton']
[1, 2, 10, 3, 4, 'JAVA', 'pyhton']

# Pop() - To delete a value from a particular index.

n = [12,4,56,7,613,624]
##n.pop(4)
##print(n)
n.pop(5)
print(n)
n.pop(0)
print(n)

##output:
##[12, 4, 56, 7, 613]
##[4, 56, 7, 613]

A = [4,5,6,"vikas",]
A.pop(3)
print(A)

output:

[4, 5, 6]


##Indexing in a List

x = [11,12,13,14,15,16,17,18,19,20]
print(x)

result1=x.index(16)

print(result1)
result2=x[9]
print(result2)

result3=x[3:8]
print(result3)

result4=x[-1:-10:-1]
print(result4)

result5=x[-3:-9:-1]
print(result5)

output:
[11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
5
20
[14, 15, 16, 17, 18]
[20, 19, 18, 17, 16, 15, 14, 13, 12]
[18, 17, 16, 15, 14, 13]

##=,copy,deepcopy

lst1 = [1,2,3,4]
lst2=lst1
print(lst1)
print(lst2)
lst1[2]=100
print(lst1)
print(lst2)
lst1.remove(4)
print(lst1)
print(lst2)

##output:
[1, 2, 3, 4]
[1, 2, 3, 4]
[1, 2, 100, 4]
[1, 2, 100, 4]
[1, 2, 100]
[1, 2, 100]


##copy
## Shallow Copy
lst1 = [1,2,3,4]

lst2 = lst1.copy()
print(lst1)
print(lst2)

lst2[2]=1000
print(lst1)
print(lst2)

lst1[2]=25
print(lst1)
print(lst2)
lst1.append(15)
print(lst1)
print(lst2)
lst1.remove(1)
print(lst1)
print(lst2)

output:

[1, 2, 3, 4]
[1, 2, 3, 4]
[1, 2, 3, 4]
[1, 2, 1000, 4]
[1, 2, 25, 4]
[1, 2, 1000, 4]
[1, 2, 25, 4, 15]
[1, 2, 1000, 4]
[2, 25, 4, 15]
[1, 2, 1000, 4]


## Shallow Copy nested list(nested list of lst1 is change then lst2 also change but append is not perform on lst 2) 

lst1=[[1,2,3,4],[5,6,7,8]]
lst2=lst1.copy()
print(lst1)
print(lst2)
lst1[1][0]=10
print(lst1)
print(lst2)
lst1.append([23,12,34])
print(lst1)
print(lst2)

output:

[[1, 2, 3, 4], [5, 6, 7, 8]]
[[1, 2, 3, 4], [5, 6, 7, 8]]
[[1, 2, 3, 4], [10, 6, 7, 8]]
[[1, 2, 3, 4], [10, 6, 7, 8]]
[[1, 2, 3, 4], [10, 6, 7, 8], [23, 12, 34]]
[[1, 2, 3, 4], [10, 6, 7, 8]]


##deep copy
import copy
lst1 = [[1,2,3,4],[4,5,6,7]]
"""
lst2 = copy.deepcopy(lst1)
print(lst1)
print(lst2)

lst1[1][0]=15
print(lst1)
print(lst2)

lst1.append("python")
print(lst1)
print(lst2)

output:
[[1, 2, 3, 4], [4, 5, 6, 7]]
[[1, 2, 3, 4], [4, 5, 6, 7]]
[[1, 2, 3, 4], [15, 5, 6, 7]]
[[1, 2, 3, 4], [4, 5, 6, 7]]
[[1, 2, 3, 4], [15, 5, 6, 7], 'python']
[[1, 2, 3, 4], [4, 5, 6, 7]]


























