
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        self.summ = 0
        def dfs(root):
            if not root:
                return
            if root.val >= low and  root.val <= high:
                self.summ += root.val
            dfs(root.left)
            dfs(root.right)    
        dfs(root)
        return self.summ


      
