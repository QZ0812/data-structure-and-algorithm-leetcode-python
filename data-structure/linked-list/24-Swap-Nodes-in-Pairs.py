# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = pre = ListNode(0)
        if not head:
            return
        if not head.next:
            return head
        
        while head and head.next:
            temp = head.next.next
            temp2 = head.next
            head.next = temp
            temp2.next = head
            pre.next = temp2
            pre = head
            head = head.next 
            
        return dummy.next
