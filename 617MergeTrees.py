# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        
        if t1 == None and t2 == None:
            return None
        
        if t1 and t2:
            node = TreeNode(t1.val + t2.val)
        if t1 and t2 == None:
            node = TreeNode(t1.val + 0)
        if t2 and t1 == None:
            node = TreeNode(t2.val + 0)
            
        node.left = self.mergeTrees(t1 and t1.left,t2 and t2.left)
        node.right = self.mergeTrees(t1 and t1.right,t2 and t2.right)
        return node
    


        

        
        