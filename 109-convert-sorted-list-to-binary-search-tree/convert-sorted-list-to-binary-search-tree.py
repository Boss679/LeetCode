# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        if not head:
            return None
        # Logn times.
        def preorder(left, right, start):
            # base case
            if left > right:
                return None
            mid = (right + left) // 2

            n = 0
            curr = prev = start
            for _ in range(mid - left):
                prev = curr
                curr = curr.next
            
            root = TreeNode(curr.val)
            root.left = preorder(left, mid - 1, start)
            root.right = preorder(mid + 1, right, curr.next)
            return root
            
        #Find size, O(n) time
        n =0
        curr = head
        while curr:
            n += 1
            curr = curr.next
        return preorder(0, n - 1, head)