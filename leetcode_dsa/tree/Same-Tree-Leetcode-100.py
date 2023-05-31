from typing import Optional
from BaseTree import TreeNode

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        """
        :i-type: class[TreeNode]
        :r-type: List[int]
        :return
        -------
        store each node inorder style from the tree and return it.

        Examples
        --------
        input:
        >>> p = [1,2,3], q = [1,2,3]
        >>> obj = Solution()
        >>> obj.isSameTree(p, q)
        output:
        >>> True
        """
        if not p and not q:
            return True
        if  not p or not q:
            return False
        else:
            return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

        
