n=int(input())
a=list(input().split())
b=[]
for i in a:
    if i not in b:
        b.append(i)
b.sort()
c=0
for i in range(len(a)):
    for j in range(len(b)):
        if a[i]==b[j]:
            c+=(j+1)
print(c)
