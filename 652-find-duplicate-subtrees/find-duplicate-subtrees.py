# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        id_map = {}
        count = defaultdict(int)
        res = []

        def dfs(node):
            if not node:
                return -1
            cur = (dfs(node.left), node.val, dfs(node.right))
            if cur not in id_map:
                id_map[cur] = len(id_map) + 1

            curId = id_map[cur]
            if count[curId] == 1:
                res.append(node)
            count[curId] += 1
            return curId

        dfs(root)
        return res