##                            Exercises
"""

#1.WAP to find the senior citizens in the given list,list values should take dynamicaly (or) from the user only.
# suppose list=[23,67,45,89,65,12,15,19], and output:[65,67,89] final list should be in accending order.
# person age is 60 (or) more than 60 belongs to senior citizens.?


list=[23,67,45,89,65,12,15,19]
print(sorted(list))
for i in sorted(list):
    if i>=60:
        print("senior citigens in the list are:",i)
        
output:

[12, 15, 19, 23, 45, 65, 67, 89]
senior citigens in the list are: 65
senior citigens in the list are: 67
senior citigens in the list are: 89
            
"""
##2.WAP to find the diagonal matrix absolute difference?
# suppose  1   2  3
#          7   9  3
#         12   5  67
#result:=>53


n = int(input().strip())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().rstrip().split())))

temp=0
emp=0

for i in range(0,len(arr)):
    temp=temp+arr[i][i]
for j in range(0,len(arr)):
    emp=emp+arr[j][len(arr)-1-j]
print((temp-emp))

output:

3
1 2 3 
7 9 3
12 5 67
53


3. WAP to solve this pattern
"""  A
     A B
     A B C
     A B C D
     A B C D E
     A B C D
     A B C
     A B
     A       






















