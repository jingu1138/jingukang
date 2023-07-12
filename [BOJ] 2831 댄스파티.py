n = int(input())

men = list(map(int,input().split()))
women = list(map(int,input().split()))

men_p, men_n, women_p, women_n = [],[],[],[]

for m in men:
    if m<0:
        men_n.append(m*(-1))
    else:
        men_p.append(m)
for w in women:
    if w<0:
        women_n.append(w*(-1))
    else:
        women_p.append(w)

men_n.sort()
men_p.sort()
women_n.sort()
women_p.sort()

cnt = 0

l,r = 0,0
while l<len(men_n) and r<len(women_p):
    m = men_n[l]
    w = women_p[r]
    if m > w:
        cnt += 1
        l, r = l+1, r+1
    else:
        l += 1
        
l,r = 0,0
while l<len(women_n) and r<len(men_p):
    m = men_p[r]
    w = women_n[l]
    if w > m:
        cnt += 1
        l, r = l+1, r+1
    else:
        l += 1

print(cnt)