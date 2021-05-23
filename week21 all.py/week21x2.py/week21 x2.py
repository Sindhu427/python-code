n=int(input())
l=list(map(int,input().split()))
if(n==len(l)):
    r=min(l)
for i in l:
    if(i==r):
        s=l.index(i)
a=str(s)
p="Dealer"+a
print(p)            