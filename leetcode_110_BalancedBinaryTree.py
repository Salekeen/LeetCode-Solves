# DO Bottom up approach
# Definition for a binary tree node.
class TreeNode:
    def __ini__(self,val=0,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import Optional


class Solution:
    def isBalanced(self, root:Optional[TreeNode]) -> bool:

        def dfs(root):
            # checking whether the tree has only one node
            if not root: return [True, 0] # [Balanced/Not, height]

            # lets call dfs on left and right subtree
            # understand this will recursively go to the bottom
            left, right = dfs(root.left) , dfs(root.right)

            balanced = (left[0] and right[0] and 
                        abs(left[1]-right[1])<=1)
            return [balanced, 1+max(left[1],right[1])]
        
        return dfs(root)[0]


