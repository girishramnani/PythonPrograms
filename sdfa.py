def ncr(n,r):
    ans = 1
    r = min(r,n-r)
    for j in range(r):
        ans *= (n-j)
        ans /= j+1
    return int(ans)
     
for i in range(int(input())):
    n , r = input().split()
    n = int(n) - 1
    r = int(r) - 1
    ans = ncr(n,r)
    print(ans) 