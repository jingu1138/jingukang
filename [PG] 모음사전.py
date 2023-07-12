import math
from itertools import product as pd
def solution(word):
    
    dic = []
    w_lst = ['A','E','I','O','U']
    for i in range(1,6):
        for c in pd(w_lst, repeat=i):
            dic.append(''.join(list(c)))
    dic.sort()
    return dic.index(word)+1

# 완전탐색은 itertool의 product나 permutation, combination을 사용할 수 있으므로 기억하자

print(math.lcm(3,5))