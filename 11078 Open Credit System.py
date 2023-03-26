#2023/3/26
#CPE Sample I/O
ans=[]
for _ in range(int(input())):
    x=input()
    l=[]
    [l.append(y)for y in input().split(" ")]
    if l[-1]=="":
        l.pop(-1)
    l=[int(y)for y in l]
    gap=l[0]-l[1]
    Max=l[0]
    for i in range(1,len(l)):
        gap=max(gap,Max-l[i])
        Max=max(Max,l[i])
    ans.append(gap)
[print(_)for _ in ans]