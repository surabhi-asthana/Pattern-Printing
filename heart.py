n=int(input("Enter number of rows: "))
m=3*n+3
x=4*n+5
j=1
for i in range(1,n+1):
     for j in range(1,x+1):
          if (((n-i+1)<=j) and (j<=(n+i+2))) or (((m-i+1)<=j) and (j<=(m+2+i))):
               print("*",end='  ')
          else:
               print(" ",end='  ') 
     print("\n")
for i in range(n+1,m+1):
     for j in range(1,x+1):
          if (j>=(i-n)) and (j<=(x-i+n+1)):
               print("*",end='  ')
          else:
               print(" ",end='  ')
     print("\n")   