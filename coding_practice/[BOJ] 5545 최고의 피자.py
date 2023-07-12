# 1원당 열량이 최고로 높은 피자
from collections import deque

n = int(input()) #토핑 종류
a,b = map(int, input().split()) #a : 도우 가격, b : 토핑 가격
c = int(input()) # c : 도우 열량
d=[]
for _ in range(n):
    d.append(int(input())) # 토핑열량 리스트

# 같은 토핑 1개만
max_value = c/a
d = sorted(d, reverse=True)
que = deque(d)
cnt = 0
cal = c
while que:
    x = que.popleft()
    cnt += 1
    cal += x
    if max(cal/(a + b*cnt),max_value) == cal/(a + b*cnt):
        max_value = cal/(a + b*cnt)
        
    else:
        cal -= x
        cnt -= 1

print(int(max_value))
