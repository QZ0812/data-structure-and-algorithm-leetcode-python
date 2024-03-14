# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Time Complexity: O(n)
# Space Complexity: O(1)
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head or not head.next:
            return None
        
        fast, slow = head, head
        m = n
        
        while m > 0:
            fast = fast.next
            m -= 1
            
        if not fast:
            return head.next
  
        while fast and fast.next:
            fast = fast.next
            slow = slow.next
        
        slow.next = slow.next.next if slow.next else None
        return head
