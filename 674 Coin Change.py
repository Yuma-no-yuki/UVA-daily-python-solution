ans=[]
coin = [1, 5, 10, 25, 50]
c = [0] * 7490
c[0] = 1
for i in range(len(coin)):
    for j in range(coin[i], int(7489) + 1):
        c[j] += c[j - coin[i]]
try:
    while True:
        m=input()
        ans.append(c[int(m)])
except EOFError:
    pass
[print(x)for x in ans]