from collections import deque
import sys
r,c,n = map(int, sys.stdin.readline().split())

stage = [list(input()) for _ in range(r)]

time = 0
bomb = deque([])
for i in range(r):
    for j in range(c):
        if stage[i][j]=='O':
            bomb.append((i,j,time))

for time in range(2,n+1):
    if time%2==0:
        for i in range(r):
            for j in range(c):
                if stage[i][j] == '.':
                    stage[i][j] = 'O'
                    bomb.append((i,j,time))
    else:
        que = bomb.copy()
        del_bomb=set()
        l = len(bomb)
        l_=0
        while l_<l:
            i,j,t = que.popleft()
            if time == t+3:
                stage[i][j]='.'
                del_bomb.add((i,j))
                if i+1<r:
                    stage[i+1][j]='.'
                    del_bomb.add((i+1,j))
                if i-1>=0:
                    stage[i-1][j]='.'
                    del_bomb.add((i-1,j))
                if j+1<c:
                    stage[i][j+1]='.'
                    del_bomb.add((i,j+1))
                if j-1>=0:
                    stage[i][j-1]='.'
                    del_bomb.add((i,j-1))
            else:
                que.append((i,j,t))
            l_+=1
        check = len(que)
        ch = 0
        while ch<check:
            i,j,t = que.popleft()
            if (i,j) in del_bomb:
                continue
            else:
                que.append((i,j,t))
            ch+=1
        bomb = que
    

for st in stage:
    for i,s in enumerate(st):
        if i<c-1:
            print(s,end='')
        else:
            print(s)