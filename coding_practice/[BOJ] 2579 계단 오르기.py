import sys

input = sys.stdin.readline

n = int(input())

score = [int(input()) for _ in range(n)]

max_v = 0
dp = [0]*(n+1)
dp[1] = score[0]
flag = 0
for i in [0,1]:
    if i == 0:
        flag = 0
    else:
        flag = 1
    while i < n-1:
        if flag != 2:
            if max(score[i],score[i+1]) == score[i]:
                dp[i+1] = dp[i] + score[i]
                i += 1
                flag += 1
            else:
                dp[i+2] = dp[i] + score[i+1]
                i += 2
                flag = 0
        else:
            dp[i+2] = dp[i] + score[i+1]
            i += 2
            flag = 0
    max_v = max(dp[-1],max_v)
print(max_v)