#2023/3/24
f_ans=[]
for _ in range(int(input())):
    s=input()
    l=[]
    ans=1
    [l.append(int(x))for x in s.split(" ")]
    l.pop(0)
    count=0
    for i in range(len(l)-1):
        if count==0:
            if l[i] > l[i+1]:
                ans+=1
            else:
                continue
        if count==1:
            if l[i] < l[i+1]:
                ans+=1
            else:
                continue
        count+=1
        if count>1:
            count=0
    f_ans.append(ans)
[print(x)for x in f_ans]