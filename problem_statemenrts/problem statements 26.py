
##                                    problem_statement.
## Given an integer,n, perform the following conditional actions:
##
##=>If  is odd, print Weird
##=>If  is even and in the inclusive range of  2 to 5 , print "Not Weird"
##=>If  is even and in the inclusive range of 6 to 20, print "Weird"
##=>If  is even and greater than 20, print "Not Weird"
 
n = int(input("enter any number: "))

if n%2==0:
    if 1<n and n<21:
        print("Not Weird")
    elif n>5 and n<21:
        print("Weird")
    elif n>20:
        print("Weird")
else:
    print("Weird")
    
output:
enter any number: 16
Not Weird
enter any number: 34
Weird
enter any number: 19
Weird
