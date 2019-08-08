n=int(input())
p=[]
a=[]
for i in range(1,n):
    cnt=0
    for j in range(1,n):
        if i%j==0:
            cnt+=1
    if cnt==2:
        p.append(i)
c=[]
for j in range(len(p)):
    for i in range(len(p)):
        if sum(c)+int(p[i])==n:
            c.append(int(p[i]))
            print(*c,sep=" ")
    c.append(int(p[j]))
