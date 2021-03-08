# https://youtu.be/Q9PIxaNGnig
from collections import defaultdict
from typing import Dict, List

keys = [
    ("A", "B"),
    ("A", "F"),
    ("B", "H"),
    ("G", "A"),
    ("G", "B"),
    ("G", "C"),
    ("D", "C"),
    ("D", "E"),
    ("D", "I"),
    ("I", "C"),
    ("E", "I"),
    ("J", "E"),
]

g = defaultdict(list)
for (k, v) in keys:
    g[k].append(v)
print(g)

visited = dict((chr(k), False) for k in range(ord("A"), ord("J") + 1))
print(visited)

def topo():
    def topo_util(node: str, visited: Dict[str, bool], stack: List):
        visited[node] = True
        for n in g[node]:
            if not visited[n]:
                topo_util(n, visited, stack)
        stack.append(node)
    
    stack = []
    for n, _ in visited.items():
        if not visited[n]:
            topo_util(n, visited, stack)

    while stack:
        print(stack.pop())

topo()



