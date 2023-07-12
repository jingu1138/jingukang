import sys
from collections import deque

input = sys.stdin.readline

tc = []
while 1:
    a,b = map(int,input().split())
    if (a,b) == (0, 0):
        break
    else:
        tc.append((a,b))

# 상근이가 무조건 적은 양 사용

def cal_elc(bill):
    use_e = 0
    bills = bill
    if bills>200:
        use_e+=100
        bills-=200
        if bills>29700:
            use_e+=9900
            bills-=29700
            if bills>4950000:
                use_e+=990000
                bills-=4950000
                if bills>0:
                    use_e+=bills/7
            else:
                use_e+=bills/5
        else:
            use_e+=bills/3
    else:
        use_e+=bills/2
    return use_e

def cal_bills(elec):
    bills = 0
    ele = elec
    if ele>100:
        bills += 2*100
        ele -= 100
        if ele > 9900:
            bills += 3*9900
            ele -= 9900
            if ele > 990000:
                bills += 5*990000
                ele -= 990000
                if ele>0:
                    bills += 7*ele
                    ele -= ele
            else:
                bills += 5*ele
        else:
            bills += 3*ele
    else:
        bills += 2*ele
    
    return bills

def bin_search(st,end,b,total_use):
    if st > end:
        return -1  # 사용량을 찾지 못한 경우 -1을 반환하거나 적절한 처리를 수행합니다.
    
    mid = (st + end) // 2
    
    diff = abs(cal_bills(mid) - cal_bills(total_use - mid))
    if diff == b:
        return min(mid, total_use - mid)
    elif diff > b:
        return bin_search(mid + 1, end, b, total_use)
    else:
        return bin_search(st, mid - 1, b, total_use)


que = deque(tc)
ans = []
while que:
    a,b = que.popleft()
    total_use = cal_elc(a)
    st, end = 0, total_use
    ans.append(cal_bills(bin_search(st,end,b,total_use)))
    
for a in ans:
    print(int(a))
