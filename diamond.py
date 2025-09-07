n=int(input("Enter number of rows: "))
x=n
m=1
for i in range(0,n):
    print(" "*x,'*'*m)
    m+=2
    x-=1
while(m>0):
    m-=2
    x+=1
    print(" "*(x+1),'*'*(m-2))