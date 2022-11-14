import sys

n = int(input())
d_lst = []
task = []
for _ in range(n):
    d, w = map(int, sys.stdin.readline().split())
    task.append((d,w))
    d_lst.append(d)
task = sorted(task, key=lambda x:x[1])
# print(task)
#일단 가중치가 높은걸 뽑지만 기한을 비교해서 뒤로 넘길수 있으면 넘기기
task_order = [0]*max(d_lst)

while task:
    day, work = task.pop()
    if task_order[day-1] < work:
        task_order[day-1] = work
    else:
        for d in range(1,day+1):
            if task_order[day-d] < work:
                task_order[day-d]=work
                break
        else:
            continue

print(sum(task_order))
