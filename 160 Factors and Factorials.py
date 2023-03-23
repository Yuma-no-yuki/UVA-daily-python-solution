#2023/3/23
ans=[]
l2=[2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97] #100以內質數(共25個)
while True:
    num=int(input())
    l = [0] * 25
    st=''
    s = ''
    if num == 0:
        break
    for t in range(2,num+1): #質因數分解，並存值至l
        for k in range(2,t+1):
            while t!=k:
                if t%k==0:
                    l[l2.index(k)]+=1
                    t=t/k
                else:
                    break
        l[l2.index(t)]+=1
    st+=('%3s'%num)
    st+='! ='
    count=0
    for x in range(len(l)):
        if l[-1]==0:
            l.pop(-1)
    if len(l)>15:
        for x in range(0,15):
            s+=('%3s'%l[x])
        s+='\n      '
        for x in range(15, len(l)):
            s+=('%3s'%l[x])
    else:
        for x in range(len(l)):
            s+=('%3s'%l[x])
    ans.append(st+s)
[print(_)for _ in ans]
