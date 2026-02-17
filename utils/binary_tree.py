from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def createTree_from_array(arr):
    root = TreeNode(val = arr[0])
    node = root
    # For each node in the tree
    left = True
    if len(arr) == 1: return root

    for i in range(1, len(arr), 1):

        if left:
            if arr[i] != None:
                node.left = TreeNode(arr[i])
        else:
            if arr[i] != None:
                node.right = TreeNode(arr[i])
            node = node.left

        left = not left

    return root

def print_tree(root: TreeNode):

    queue = deque([root])

    print("[", end="")

    while queue:
        node = queue.popleft()
        
        if not node:
            print("None", end=", ")
        else:
            queue.append(node.left)
            queue.append(node.right)
            print(node.val, end=", ")

    print("]")