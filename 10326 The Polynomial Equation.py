#2023/3/27
ans=[]
try:
    while True:
        t=input()
        x=[]
        [x.append(y)for y in input().split(" ")]
        if x[-1] == "":
            x.pop(-1)
        x=[-int(y)for y in x]
        dp=[[0] * len(x) for i in range(len(x))]
        dp[0][0]=x[0]
        for i in range(1, len(x)):
            for j in range(len(x)):
                if j==0:
                    dp[i][j]=dp[i-1][j]+x[i]
                else:
                    dp[i][j]=x[i]*(dp[i-1][j-1])+dp[i-1][j]
        s = ""
        s += f"x^{t} + "
        for i in range(len(dp[-1])):
            if dp[-1][i] != 0:
                s += f"{dp[-1][i]}x^{len(dp[-1]) - 1 - i} + "
        if dp[-1][-1] == 0:
            s += "0 "
        s = s.replace("x^0 +", "")
        s = s.replace("+ -", "- ")
        s = s.replace(" 1x", " x")
        s = s.replace("x^1 ", "x ")
        s += "= 0"
        ans.append(s)
except EOFError:
    pass
[print(get)for get in ans]