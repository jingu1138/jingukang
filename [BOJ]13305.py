import sys

n = int(input())

edge_lst = list(map(int,sys.stdin.readline().split()))
node_lst = list(map(int,sys.stdin.readline().split()))

min_gas = node_lst[0]
bill = 0
for i in range(n-1):
  if min(node_lst[i],min_gas) == node_lst[i]:
    min_gas = node_lst[i]
  bill += edge_lst[i]*min_gas
print(bill)
