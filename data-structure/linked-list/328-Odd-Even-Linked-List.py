# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# O(1) space complexity and O(n) time complexity
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        odd, even = head, head.next
        dummy = even
        
        while odd and even:
            # we need to stop before odd reach to None
            if odd.next.next:
                odd.next = odd.next.next
                odd = odd.next
            # we need to move until even reach to None
            even.next = even.next.next if even.next else None
            even = even.next
        
        odd.next = dummy
        
        return head
