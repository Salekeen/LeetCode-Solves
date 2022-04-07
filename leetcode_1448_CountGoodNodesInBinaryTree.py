# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node,maxVal):
            # BASE cASE
            if not node:
                return 0
            # for the root case
            res = 1 if node.val>= maxVal else 0
            # update the max value as we need to pass it along the path
            maxVal = max(maxVal,node.val)

            res+= dfs(node.left,maxVal)
            res+= dfs(node.right, maxVal)

            return res
        return dfs(root, root.val)
