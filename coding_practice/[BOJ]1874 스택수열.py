import sys

input = sys.stdin.readline
n = int(input())

ans_lst = []
for _ in range(n):
    ans_lst.append(int(input()))

stack = []
ans = []
idx = 0
for i in range(1,n+1):
    if stack and stack[-1] == ans_lst[idx]:
        stack.pop()
        ans.append('-')
        idx += 1
    else:
        stack.append(i)
        ans.append('+')

for s in stack[::-1]:
    print(s)
    if s == ans_lst[idx]:
        ans.append('-')
        idx += 1
    else:
        ans.append('no')

print(ans)
if 'no' in ans:
    print('NO')
else:
    for a in ans:
        print(a)











# i = 1
# if len(set(ans_lst)) == len(ans_lst):
#     lst.append(i)
#     i += 1
#     answer.append('+')
#     while lst:
#         if lst and lst[-1] == ans_lst[idx]:
#             ans.append(lst.pop())
#             answer.append('-')
#             idx += 1
#         else:
#             lst.append(i)
#             answer.append('+')
#             i += 1

# if ans != ans_lst:
#     print('No')
# else:
#     for a in answer:
#         print(a)