n,m=map(int,input().split())
l=list(map(int,input().split()))
k=list(map(int,input().split()))
r=[]
if(n==len(l) and m==len(k)):
    l.sort()
    k.sort(reverse=True)
for i in l:
    r.append(i)
for i in k:
    r.append(i)
print(*r)