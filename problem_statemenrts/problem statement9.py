n=int(input("Enter the number"))
for row in range(1,n+1): 
    c_sum=0     
    for i in range(1,row+1): 
        c_sum=c_sum+i 
        if i<row: 
            print(i,'+',sep='',end='') 
        else: 
            print(i,sep='',end='') 
    print('=',c_sum,sep='') 


output:

Enter the number10
1=1
1+2=3
1+2+3=6
1+2+3+4=10
1+2+3+4+5=15
1+2+3+4+5+6=21
1+2+3+4+5+6+7=28
1+2+3+4+5+6+7+8=36
1+2+3+4+5+6+7+8+9=45
1+2+3+4+5+6+7+8+9+10=55
