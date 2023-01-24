# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        level = 0
        queue = deque()
        res = []

        if root:
            # If root exists -> place inside array and append
            queue.append(root)

        while len(queue) > 0:
            arr = []
            # Loop through the level and append each entry to arr
            for el in range(len(queue)):
                curr = queue.popleft()
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
                # Append the value of the left-most element that you popped to arr
                arr.append(curr.val)
            # Append arr to final result
            res.append(arr)
            level += 1

        return res
