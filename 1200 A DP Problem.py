#2023/4/9
ans=[]
for _ in range(int(input())):
    s=input()
    if s[0]=='x':
        s=' '+s
    s=s.replace('+x','+1x')
    s=s.replace('-x','-1x')
    s=s.replace(' x','1x')
    s=s.replace('=x','=1x')
    s1,s2=s.split("=")
    l=[0,0,0,0] #a b c d => ax+b=cx+d
    ll = ''
    s1+='='
    s2+='='
    for i in range(len(s1)):
        ll+=s1[i]
        if s1[i] == 'x':
            if ll[:-1] != "":
                l[0]+=int(ll[:-1])
            ll=''
        if s1[i] == '-':
            if ll[:-1] != "":
                l[1] += int(ll[:-1])
            ll='-'
        if s1[i] == '+'or s1[i] == '=':
            if ll[:-1]!="":
                l[1] += int(ll[:-1])
            ll=''
    for i in range(len(s2)):
        ll+=s2[i]
        if s2[i] == 'x':
            if ll[:-1]!="":
                l[2]+=int(ll[:-1])
            ll=''
        if s2[i] == '-':
            if ll[:-1] != "":
                l[3] += int(ll[:-1])
            ll='-'
        if s2[i] == '+'or s2[i] == '=':
            if ll[:-1]!="":
                l[3] += int(ll[:-1])
            ll=''
    if l[0]==l[2]and l[1]==l[3]:
        ans.append('IDENTITY')
    elif l[0]==l[2]and l[1]!=l[3]:
        ans.append('IMPOSSIBLE')
    else:
        ans.append((l[1]-l[3])//(l[2]-l[0]))
[print(_)for _ in ans]