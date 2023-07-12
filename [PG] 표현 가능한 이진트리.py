answer = []
numbers = list(map(int,input().split()))

def recursion(s):
    n = len(s)
    mid_idx = n // 2
    if s[mid_idx] == '1':  # 중간 글자가 1인 경우
        if n <= 3:  # 길이가 3이하인 경우 True 반환
            return True
        else:  # 왼쪽과 오른쪽 부분 문자열에 대해 재귀호출
            left = s[:mid_idx]
            right = s[mid_idx+1:]
            return recursion(left) and recursion(right)
    else:  # 중간 글자가 0인 경우 False 반환
        return False

for num in numbers:
    s = bin(num)[2:]
    
    for i in range(7):
        if len(s) <= (2**i)-1:
            s = '0'*((2**i)-1 - len(s)) + s
            break
    print(s)
    if '1' not in s[:len(s)//2] and s[len(s)//2]=='1':
        s = s[len(s)//2+1:]
    flag = recursion(s)
    if flag == True:
        answer.append(1)
    else:
        answer.append(0)

print(answer)