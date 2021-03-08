from collections import defaultdict

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

visited = [False for _ in keys]

def dfs(at):
    if visited[at]: return
    print("visiting", at)
    visited[at] = True

    neighbor = g[at]
    for n in neighbor:
        dfs(n)

if __name__ == "__main__":
    dfs(0)