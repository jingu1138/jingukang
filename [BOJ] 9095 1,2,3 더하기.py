import sys

input = sys.stdin.readline

n = int(input())

dp = [0]*(11)
dp[1] = 1
dp[2] = 2
dp[3] = 4

num = []
for _ in range(n):
    num.append(int(input()))
    
for i in range(4,11):
    dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

for n in num:
    print(dp[n])
# 1+1+1+1+1+1
# 1+1+1+1+2
# 1+1+1+2+1
# 1+1+2+1+1
# 1+2+1+1+1
# 2+1+1+1+1
# 1+1+1+3
# 1+1+3+1
# 1+3+1+1
# 3+1+1+1
# 1+2+3
# 1+3+2
# 3+1+2
# 3+2+1
# 2+1+3
# 2+3+1
# 2+2+2
# 3+3
