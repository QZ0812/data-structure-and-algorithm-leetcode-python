# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next



class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        # split
        slow = ListNode(0, head)
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        temp = slow.next
        slow.next = None

        l = self.sortList(head)
        r = self.sortList(temp)
        # merge and sort
        return self.mergeList(l, r)
        
    
    def mergeList(self, list1, list2):
        dummy = ans = ListNode(0)
        
        while list1 and list2:
            if list1.val > list2.val:
                dummy.next = list2
                list2 = list2.next
            else:
                dummy.next = list1
                list1 = list1.next
            dummy = dummy.next
    
        dummy.next = list1 if list1 else list2

        return ans.next
