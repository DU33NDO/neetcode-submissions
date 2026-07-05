# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def getSuccessor(curr):
            curr = curr.right
            while curr is not None and curr.left is not None:
                curr = curr.left
            return curr

        if not root:
            return root
        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        else:
            if root.right is None:
                return root.left
            if root.left is None:
                return root.right 
            if root.left and root.right:
                succ = getSuccessor(root)
                root.val = succ.val
                root.right = self.deleteNode(root.right, succ.val)
        return root



                
        