
from collections import defaultdict, deque
from typing import List

keys = [
    (0, 5),
    (4, 3),
    (0, 1),
    (9, 12),
    (6, 4),
    (5, 4),
    (0, 2),
    (11, 12),
    (9, 10),
    (0, 6),
    (7, 8),
    (5, 3),
]

n = len(keys)
g = defaultdict(list)

for (k,v) in keys:
    g[k].append(v)

print("The graph is", g)

def bfs(start: int):
    # can be use to recontruct paths
    prev = [None for _ in keys]
    visited = [False for _ in keys]
    visited[start] = True

    q = deque([])
    q.append(start)

    print("Visiting", start)
    while q:
        node = q.popleft()
        for n in g[node]:
            if not visited[n]:
                q.append(n)
                print("Visiting", n)
                visited[n] = True
                prev[n] = n
    return prev
    

if __name__ == "__main__":
    ret = bfs(0)
    print(ret)




