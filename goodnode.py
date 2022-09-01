#Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # log highest value
        highest = root.val

        # we always have 1, as our restrictions are that the tree must have 1 node, and root is considered a good node
        # recurse through both paths
        count = 1 + self.isGoodNode(root.left, highest) + self.isGoodNode(root.right, highest)

        return count

    def isGoodNode(self, node, highest):
        # if our current node value is higher or eq to highest, we add 1 to good nodes
        goodNode = 0

        if not node:
            return 0

        if node.val >= highest:
            goodNode = 1
            highest = node.val

        # we traverse left and right fields
        if node.left:
            goodNode = goodNode + self.isGoodNode(node.left, highest)

        if node.right:
            goodNode = goodNode + self.isGoodNode(node.right, highest)

        return goodNode


[9,null,3,6]
test_tree = TreeNode(9, )
print(Solution().goodNodes(test_tree))