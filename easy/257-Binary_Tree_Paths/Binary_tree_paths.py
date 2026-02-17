from typing import Optional, List
from utils.binary_tree import *

class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        
        output = []
        
        def nextNode(node : TreeNode, string : str):
            """
            Recursive function
            """

            # if node is leaf it has no childs
            if (not node.left) and (not node.right):
                output.append(string + str(node.val))
            else:
                # If not for each node add the corresponding string
                if node.left:
                    nextNode(node.left, string + str(node.val) + "->")
                if node.right:
                    nextNode(node.right, string + str(node.val) + "->")
            
        nextNode(root, "")

        return output
    
# $env:PYTHONPATH = (Get-Location)