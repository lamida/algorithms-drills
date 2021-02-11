# https://www.youtube.com/watch?v=uWL6FJhq5fM&ab_channel=VivekanandKhyade-AlgorithmEveryDay
class Tree:
    def __init__(self, val: int, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def bfs(root: Tree):
    q = []
    q.append(root)
    while(len(q) > 0):
        root = q.pop(0)
        print(root.val)
        if root.left:
            q.append(root.left)
        if root.right:
            q.append(root.right)

def dfs(root: Tree):
    if root:
        print(root.val)
        dfs(root.left)
        dfs(root.right)

if __name__ == "__main__":
    t = Tree(1, Tree(2, Tree(10), Tree(20)), Tree(3, Tree(100), Tree(200)))
    print("bfs")
    bfs(t)
    print("dfs")
    dfs(t)
