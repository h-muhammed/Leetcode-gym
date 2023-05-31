from typing import List, Optional
from BaseTree import TreeNode


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """
        :i-type: class[TreeNode]
        :r-type: List[int]
        :return
        -------
        store each node inorder style from the tree and return it.

        Examples
        --------
        input:
        >>> root = [1,null,2,3]
        >>> obj = Solution()
        >>> obj.inorderTraversal(root)
        output:
        >>> [1,3,2]
        """

        if not root:
            return root
        nodes = []
        def inorder(root):
            if root:
                inorder(root.left)
                nodes.append(root.val)
                inorder(root.right)
            else:
                return None
        inorder(root)
        return nodes

if __name__ == '__main__':
    
    head = TreeNode()
    root = TreeNode(1)
    root = head.constructTree(root, None)
    root = head.constructTree(root, 2)
    root = head.constructTree(root, 3)

    obj = Solution()
    print(obj.inorderTraversal(root))
        