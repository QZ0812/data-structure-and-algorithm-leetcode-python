# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# iterative 
# Time Complexity: O(n)
# Space Complexity: O(1)
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ans = ListNode(0)
        
        while list1 and list2:                
            if list1.val < list2.val:
                dummy.next = ListNode(list1.val)
                list1 = list1.next
            else:
                dummy.next = ListNode(list2.val)
                list2 = list2.next
            dummy = dummy.next
                
        if list1 or list2:
            dummy.next = list1 or list2

        return ans.next
