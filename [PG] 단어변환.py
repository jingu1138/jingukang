from collections import defaultdict, deque
def bfs(graph, visited, st, end, cnt):
    
    que = deque([(st,end,cnt)])
    
    while que:
        st, end, cnt = que.popleft()
        visited[st] = True
        
        if end in graph[st]:
            cnt += 1
            st = end
            break
        else:
            for g in list(graph[st]):
                if visited[g] == False:
                    que.append((g,end,cnt+1))
    if st!=end:
        cnt = 0
    
    return cnt


def dif_count(w1,w2):
    count = 0
    w1_lst = list(w1)
    w2_lst = list(w2)
    
    for w_ in w1_lst:
        if w_ not in w2_lst:
            count += 1
    return count

begin = 'hit'
target = 'cog'
words = ["hot", "dot", "dog", "lot", "log", "cog"]
visited = {}
for w in words:
    visited[w] = False
        
graph = defaultdict(set)
    
for w in words:
    for v in words:
        if dif_count(w,v) == 1:
            graph[w].add(v)
            graph[v].add(w)

for w in words:
    if dif_count(w, begin) == 1:
        begin = w
        break


print(bfs(graph, visited, begin, target, 1))