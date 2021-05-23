n=int(input())
m=list(map(int,input().split()))
li=[]
for i in m:
    if i not in li:
        li.append(i)
a=max(li)
li.remove(a)
b=max(li)
print(b)
