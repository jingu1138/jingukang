import sys
import heapq
from collections import defaultdict

input = sys.stdin.readline

n,d  = map(int, input().split())
graph = defaultdict(list)
distance = [i for i in range(d+1)]
start = 0

for i in range(n):
    s,e,d = map(int, input().split())
    graph[s].append((d,e))
    
# 다익스트라 함수 구현
def dijkstra(start):
    q = []
    heapq.heappush(q,(0, start))
    distance[start] = 0
    while q:
        dis, now = heapq.heappop(q)
        if distance[now] < dis:
            continue
        
        for i in graph[now]:
            cost = dis + i[1]
            if i[1] <= d and cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))

dijkstra(start)

print(distance[-1])


   
   