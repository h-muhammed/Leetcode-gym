from typing import List, Optional
from BaseTree import TreeNode


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> List[int]:
        """
        :i-type: class[TreeNode]
        :r-type: List[int]
        :return
        -------
        store each node inorder style from the tree and return it.

        Examples
        --------
        input:
        >>> nodes = [4,2,7,1,3,6,9]
        >>> obj = Solution()
        >>> obj.inorderTraversal(root)
        output:
        >>> [1,3,2]
        """
        if root == None:
            return None
        self.invertTree(root.left)
        self.invertTree(root.right)
        tempNode = root.left
        root.left = root.right
        root.right = tempNode 

        return root 

if __name__ == '__main__':
    
    head = TreeNode()
    Nodes = [4,2,7,1,3,6,9]
    root = TreeNode(Nodes[0])
    for idx in range(1, len(Nodes)):
        root = head.constructTree(root, root[idx])    
    obj = Solution()
    print(obj.postorderTraversal(root)) 