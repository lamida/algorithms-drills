class Tree:
    def __init__(self, vl: int, left: "Tree"= None, right: "Tree" = None):
        self.vl = vl
        self.left = left
        self.right = right

from collections import deque, defaultdict

q = deque()
lvlv = defaultdict(list) 
def bfs(root: Tree, lv = 0):
    if root is None: return

    lvlv[lv].append(root.vl)
    q.append(root)
    while q:
        current = q.popleft()
        bfs(root.left, lv + 1)
        bfs(root.right, lv + 1)

t = Tree(4, Tree(7, Tree(10), Tree(2, None, Tree(6, Tree(2)))), Tree(9, None, Tree(6)))
bfs(t)
ll = []
for k, v in lvlv.items():
    ll .append(int(sum(v)/len(v)))
print(ll)



