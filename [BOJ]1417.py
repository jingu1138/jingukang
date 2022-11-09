lst = []
p_lst = []
n = int(input())
for i in range(n):
    lst.append(int(input()))
p = lst[0]
if len(lst)>1:
    p_lst = lst[1:]
cnt = 0

i = 0
if p_lst:
    while max(p_lst) >= p:
        if p_lst[i] == max(p_lst):
            p_lst[i] -= 1
            p += 1
            cnt += 1
        else:
            if i<n-2:
                i += 1
            else:
                i = 0
print(cnt)
