n = 7
c=0
a = [[(n-i+j)*(i >= j) for i in range(n,c,-1)] for j in range(1,n+1)]
for r in a:
    print(*r)
