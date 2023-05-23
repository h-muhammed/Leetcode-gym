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