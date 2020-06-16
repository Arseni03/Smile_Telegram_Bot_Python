i=0
j=0
s=0
a=[]
n = int(input())
for i in range(n):
     a.append([2]*n)
print(a)
for i in range(n):
   for j in range(n-i):
      a[i][j]=1
for i in range(n):
   for j in range(n-i-1):
      a[i][j]=0
print(a)


