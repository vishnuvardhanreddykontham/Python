"""
##1.Write a program which will find all such numbers which are divisible by 7 but
##are not a multiple of 5, between 2000 and 3200 (both included).
##
upper=2000
lower=3200
for x in range(2000,3200):
    if x%7==0 and x%5!=0:
        print(x,end=",")
else:
    print("error")

output:
2002,2009,2016,2023,2037,2044,2051,2058,2072,2079,2086,2093,2107,2114,2121,2128,2142,2149,2156,2163,2177,2184,2191,
2198,2212,2219,2226,2233,2247,2254,2261,2268,2282,2289,2296,2303,2317,2324,2331,2338,2352,2359,2366,2373,2387,2394,
2401,2408,2422,2429,2436,2443,2457,2464,2471,2478,2492,2499,2506,2513,2527,2534,2541,2548,2562,2569,2576,2583,2597,
2604,2611,2618,2632,2639,2646,2653,2667,2674,2681,2688,2702,2709,2716,2723,2737,2744,2751,2758,2772,2779,2786,2793,
2807,2814,2821,2828,2842,2849,2856,2863,2877,2884,2891,2898,2912,2919,2926,2933,2947,2954,2961,2968,2982,2989,2996,
3003,3017,3024,3031,3038,3052,3059,3066,3073,3087,3094,3101,3108,3122,3129,3136,3143,3157,3164,3171,3178,3192,3199,error


##2.Write a program which can compute the factorial of a given numbers.
##The results should be printed in a comma-separated sequence on a single line.
##Suppose the following input is supplied to the program:
##8
##Then, the output should be:
##40320

num=int(input("Enter number: "))
factorial=1
for i in range(1,num+1):
    factorial=factorial*i
print(factorial,end="")

output:
Enter number: 8
40320

##3.With a given integral number n, write a program to generate a dictionary that contains (i, i*i) such
##that is an integral number between 1 and n (both included). and then the program should print the dictionary.
##Suppose the following input is supplied to the program:
##8
##Then, the output should be:
##{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}

num=int(input("Enter number: "))
x=dict()
for i in range(1,num+1):
    x[i]=i*i
print(x)

##output:
##Enter number: 8
##{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}

##4.Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number.
##Suppose the following input is supplied to the program:
##34,67,55,33,12,98
##Then, the output should be:
##['34', '67', '55', '33', '12', '98']
##('34', '67', '55', '33', '12', '98')

num= list(map(str,input().split()))

print(num)

print(tuple(num))

output:
34,67,55,33,12,98
['34,67,55,33,12,98']
('34,67,55,33,12,98',)

5.Define a class which has at least two methods:
getString: to get a string from console input
printString: to print the string in upper case.
Also please include simple test function to test the class methods.


##Write a program that calculates and prints the value according to the given formula:
##Q = Square root of [(2 * C * D)/H]
##Following are the fixed values of C and H:
##C is 50. H is 30.
##D is the variable whose values should be input to your program in a comma-separated sequence.
##Example
##Let us assume the following comma separated input sequence is given to the program:
##100,150,180
##The output of the program should be:
##18,22,24

num= list(map(int,input().split(" ")))
C=50
H=30
for i in num:
    Q=((2*C*i)/H)**(0.5)
    print(int(Q),end=",")    

output:
100 150 180
18,22,24 

##7.Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array.
##The element value in the i-th row and j-th column of the array should be i*j.
##Note: i=0,1.., X-1; j=0,1,¡­Y-1.
##Example
##Suppose the following inputs are given to the program:
##3,5
##Then, the output of the program should be:
##[[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]] 

x=int(input("enter number: "))
y=int(input("enter number: "))
ls=list()
for i in range(0,x):
    ls1=[]
    for j in range(0,y):
        ls1.append(i*j)
    ls.append(ls1)
print(ls)

output:
enter number: 3
enter number: 5
[[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]

##8.Write a program that accepts a comma separated sequence of words as input and
##prints the words in a comma-separated sequence after sorting them alphabetically.
##Suppose the following input is supplied to the program:
##without,hello,bag,world
##Then, the output should be:
##bag,hello,without,world

st= map(str,input().split(","))

print(",".join(sorted(st)))

output:

without,hello,bag,world
bag,hello,without,world
 
##
##9.Write a program that accepts sequence of lines as input and prints the lines after making all characters
##in the sentence capitalized.
##Suppose the following input is supplied to the program:
##Hello world
##Practice makes perfect
##Then, the output should be:
##HELLO WORLD
##PRACTICE MAKES PERFECT





##12.Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each digit
##of the number is an even number.
##The numbers obtained should be printed in a comma-separated sequence on a single line.
##
for item in range(1000,3001):
    if  all(int(i)%2==0 for i in str(item)):
        print(item,end=",")

output:

2000,2002,2004,2006,2008,2020,2022,2024,2026,2028,2040,2042,2044,2046,2048,2060,2062,2064,2066,2068,2080,2082,2084,
2086,2088,2200,2202,2204,2206,2208,2220,2222,2224,2226,2228,2240,2242,2244,2246,2248,2260,2262,2264,2266,2268,2280,
2282,2284,2286,2288,2400,2402,2404,2406,2408,2420,2422,2424,2426,2428,2440,2442,2444,2446,2448,2460,2462,2464,2466,
2468,2480,2482,2484,2486,2488,2600,2602,2604,2606,2608,2620,2622,2624,2626,2628,2640,2642,2644,2646,2648,2660,2662,
2664,2666,2668,2680,2682,2684,2686,2688,2800,2802,2804,2806,2808,2820,2822,2824,2826,2828,2840,2842,2844,2846,2848,
2860,2862,2864,2866,2868,2880,2882,2884,2886,2888,

"""
##
##13.Write a program that accepts a sentence and calculate the number of letters and digits.
##Suppose the following input is supplied to the program:
##hello world! 123
##Then, the output should be:
##LETTERS 10
##DIGITS 3

ip=input("enter anything: ")
d=0
l=0
for i in ip:
    
    if i.isnumeric():
        d=d+1
    elif i.isalpha():
        l=l+1
    else:
        pass
print("LETTERS",l)
print("DIGITS",d)

output:

enter anything: hello world 123
LETTERS 10
DIGITS 3



















































