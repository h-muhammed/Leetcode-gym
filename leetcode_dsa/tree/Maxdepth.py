from typing import List, Optional
from BaseTree import TreeNode


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        """
        :i-type: class[TreeNode]
        :r-type: List[int]
        :return
        -------
        store each node inorder style from the tree and return it.

        Examples
        --------
        input:
        >>> nodes = [3,9,20,None,None,15,7]
        >>> obj = Solution()
        >>> obj.inorderTraversal(root)
        output:
        >>> 3
        """
        if not root:
            return 0
        return 1+max(self.maxDepth(root.left), self.maxDepth(root.right))

if __name__ == '__main__':
    
    head = TreeNode()
    Nodes = [3,9,20,None,None,15,7]
    root = TreeNode(Nodes[0])
    for idx in range(1, len(Nodes)):
        root = head.constructTree(root, root[idx])    
    obj = Solution()
    print(obj.maxDepth(root)) 