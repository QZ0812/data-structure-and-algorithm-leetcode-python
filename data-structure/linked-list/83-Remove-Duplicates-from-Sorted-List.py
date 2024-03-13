# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Time Complexity: O(n)
# Space Complexity: O(1)
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = ans = ListNode(float(-inf))
        prev.next = ans = head
        
        while head:
            while head and prev.val == head.val:
                head = head.next
            prev.next = head

            if head:
                prev = head
                head = head.next
            
        return ans
