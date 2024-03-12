# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next



# recursion 
# Time Complexity: O(n)
# Space Complexity: O(n)
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def dfs(head, pre):
            if not head:
                return pre
            post = head.next
            head.next = pre
            
            return dfs(post, head)
            
        return dfs(head, None)



# iterative 
# Time Complexity: O(n)
# Space Complexity: O(1)
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pre, cur = None, head
        while cur:
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt
            
        return pre



