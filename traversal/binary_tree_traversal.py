from collections import deque

class TreeNode:
    def __init__(self, val: int, left: "TreeNode" = None, right: "TreeNode" = None):
        self.val = val
        self.left = left
        self.right = right

def preorder(root: TreeNode):
    if root:
        print(root.val)
        preorder(root.left)
        preorder(root.right)

def preorder_iter(root: TreeNode):
    """
    without recursion we will simulate the call stack using ...
    stack data structure.

    One thing to note is, when pushing to the stack, we reverse the sequence
    by pushing right first before left, so that when it is pop, left tree
    will be processed first.
    """
    
    stack = []
    stack.append(root)
    while stack:
        current = stack.pop()
        print(current.val)
        # push right first intead of left
        if current.right:
            stack.append(current.right)
        if current.left:
            stack.append(current.left)

def postorder(root: TreeNode):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.val)

def inorder(root: TreeNode):
    if root:
        inorder(root.left)
        print(root.val)
        inorder(root.right)

def bfs(root: TreeNode):
    q = deque()
    q.append(root)
    while q:
        current = q.popleft()
        # Process the tree
        print(current.val)
        if current.left:
            q.append(current.left)
        if current.right:
            q.append(current.right)

if __name__ == "__main__":
    # https://en.wikipedia.org/wiki/Binary_tree#:~:text=In%20computer%20science%2C%20a%20binary,child%20and%20the%20right%20child.
    # Replace the root with 1
    tree = TreeNode(1, TreeNode(7, TreeNode(2), TreeNode(6, TreeNode(5), TreeNode(11))), TreeNode(5, None, TreeNode(9, TreeNode(4))))
    print("preorder")
    preorder(tree)

    print("preorder_iter")
    preorder_iter(tree)

    print("postorder")
    postorder(tree)

    print("inorder")
    inorder(tree)

    print("bfs")
    bfs(tree)