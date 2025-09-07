n=int(input("Enter number of rows: "))
x=n*(n+1)//2
for i in range(n):
    for j in range(i,n):
        print(x,end='')
        x-=1
    print('')