class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data
class Solution:
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root

    def getHeight(self,root):
        #Write your code here
        if not root:
            return -1
        if not root.left and not root.right:
            return 0

        leftHeight = self.getHeight(root.left)
        rightHeight = self.getHeight(root.right)

        return max(leftHeight,rightHeight)+1

T=int(input())