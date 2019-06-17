import sys

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

    def levelOrder(self,root):
        #Write your code here
        nodeToSearch = list()
        nodesTraversed = ''
        nodeToSearch.append(root)
        while len(nodeToSearch)>0:
            node = nodeToSearch.pop(0)
            if node.left:
                nodeToSearch.append(node.left)
            if node.right:
                nodeToSearch.append(node.right)

            nodesTraversed += str(node.data) + ' '
        print(nodesTraversed)

T=int(input())
myTree=Solution()
root=None
for i in range(T):
    data=int(input())
    root=myTree.insert(root,data)
myTree.levelOrder(root)
