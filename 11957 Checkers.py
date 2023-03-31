#2023/3/31
#TLE...
ans=[]
for t2 in range(int(input())):
    l2=[]
    c=0
    for t1 in range(int(input())):
        s=input()
        if c==0:
            if 'W' in s:
                l2.append(list(s))
                c=1
            else:
                l2.append(list(s))
    l=[]
    b=[]
    for i in range(len(l2)):
        for j in range(len(l2[0])):
            if l2[i][j] == '.':
                l2[i][j]= 0
            if l2[i][j] == 'W':
                l2[i][j]= 1
            if l2[i][j] == "B":
                l2[i][j] = 0
                b.append([len(l2)-i-1,j])
    for i in range(len(l2)):
        l.append(l2[-(i+1)])
    for i in range(1,len(l)):
        for j in range(len(l[0])):
            if i-1>=0 and j-1 >=0 and j+1<= len(l[0])-1:
                if [i - 1, j - 1] in b:
                    l[i - 1][j - 1] = 0
                    if i - 2 >= 0 and j - 2 >= 0:
                        l[i][j] += l[i - 2][j - 2]
                if [i - 1, j + 1] in b:
                    l[i - 1][j + 1] = 0
                    if i - 2 >= 0 and j + 2 <= len(l[0]) - 1:
                        l[i][j] += l[i - 2][j + 2]
                l[i][j]+=l[i-1][j-1]+l[i-1][j+1]
            elif i-1>=0 and j-1>=0:
                if[i-1,j-1] in b:
                    l[i - 1][j - 1]=0
                    if i-2>=0 and j-2>=0:
                        l[i][j]+=l[i-2][j-2]
                l[i][j]+=l[i-1][j-1]
            elif i-1>=0 and j+1 <= len(l[0])-1:
                if [i-1,j+1] in b:
                    l[i - 1][j + 1] = 0
                    if i - 2 >= 0 and j + 2 <= len(l[0]) - 1:
                        l[i][j] += l[i - 2][j + 2]

                l[i][j]+=l[i-1][j+1]
            else:
                continue
            if [i,j]in b :
                l[i][j]=0
    ss=sum(l[-1])
    if ss>1000007:
        ss%=1000007
    ans.append(ss)
for _ in range(len(ans)):
    print(f"Case {_+1}: {ans[_]}")