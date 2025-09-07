def generate(numRows):
    a=[[1]]
    for i in range(0,numRows-1):
        b=[]
        for j in range(0,len(a[i])+1):
            if j==0 or j==len(a[i]):
                b.append(1)
            else:
                b.append(a[i][j]+a[i][j-1])
        a.append(b)
    return(a)
n=int(input("Enter number of rows: "))
a=generate(n)
x=n-1
for i in range(0,len(a)):
    print(" "*x,a[i])
    x-=1

    





        
        

