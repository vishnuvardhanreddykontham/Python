##                                        problem statement

##Write a Python program to find the strings in a given list, starting with a given prefix.
##Input: [( ca,('cat', 'car', 'fear', 'center'))] Output: ['cat', 'car']
##Input: [(do,('cat', 'dog', 'shatter', 'donut', 'at', 'todo'))] Output: ['dog', 'donut']
##

ls=list(map(str,input("Enter the String ").split(" ")))
starts_with=input("Enter the String you want to starts with ").strip()
for i in ls:
    if i.startswith(starts_with):
        print(i)

##output:
Enter the String vishnu vinay venkat venu
Enter the String you want to starts with vi
vishnu
vinay
