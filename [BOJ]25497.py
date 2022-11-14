n = int(input())
skill=input()
cnt = 0
s_idx = []
l_idx = []
for i in range(n):
  if skill[i].isdigit():
    cnt+=1
    continue
  else:
    if skill[i] == 'S':
      s_idx.append(i)
    elif skill[i] == 'L':
      l_idx.append(i)
    elif skill[i] == 'K':
      if s_idx:
        s_idx.pop(-1)
        cnt+=1
      else:
        break
    elif skill[i] == 'R':
      if l_idx:
        l_idx.pop(-1)
        cnt+=1
      else:
        break

print(cnt)
