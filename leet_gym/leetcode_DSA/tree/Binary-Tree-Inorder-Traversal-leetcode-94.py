from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        """
        Initialize Tree object from input root and child representation.

        Parameters
        ----------
        val
            value of a node.
        left
            left child of the tree.
        right
            right child of the tree.
        
        """
        self.val = val
        self.left = left
        self.right = right


    # Insert a node
    def constructTree(self, node, val):

        """
        Return a new node if the tree is empty
        """
        if val is None:
            return node
        if node is None:
            return TreeNode(val)
        if val < node.val:
            node.left = self.constructTree(node.left, val)
        else:
            node.right = self.constructTree(node.right, val)

        return node

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
        