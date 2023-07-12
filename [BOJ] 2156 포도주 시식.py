import sys

input = sys.stdin.readline

n = int(input())
lst = []

for _ in range(n):
    lst.append(int(input()))

dp = [0]*(n+1)

flag = 0

for i in range(1,n+1):
    if flag != 2:
        if max(dp[i-1], dp[i-2]) == dp[i-1]:
            dp[i] = dp[i-1] + lst[i-1]
            flag += 1
        else:
            dp[i] = dp[i-2] + lst[i-1]
            flag = 1
    else:
        dp[i] = dp[i-1]
        flag = 0
print(dp[-1])
