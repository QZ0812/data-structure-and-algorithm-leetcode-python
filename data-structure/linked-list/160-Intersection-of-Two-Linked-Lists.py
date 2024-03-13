# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# method one
# Time Complexity: O(n+m): n is first linked list lenth, m is second linked list lenth
# Space Complexity: O(1)
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        l1, l2 = headA, headB
        while l1 != l2:
            l1 = l1.next if l1 else headB
            l2 = l2.next if l2 else headA
            
        return l1


# method two
# Time Complexity: O(n+m): n is first linked list lenth, m is second linked list lenth
# Space Complexity: O(1)
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if not headA:
            return None
        if not headB:
            return None
        
        l1, l2 = headA, headB
        len1, len2 = 0, 0
        while l1:
            len1 += 1
            l1 = l1.next
        while l2:
            len2 += 1
            l2 = l2.next
 
        if len1 > len2:
            diff = len1 - len2
            while diff > 0:
                headA = headA.next
                diff -= 1
        elif len1 < len2:
            diff = len2 - len1
            while diff > 0:
                headB = headB.next 
                diff -= 1
       
        while headA and headB:
            if headA == headB:
                return headA
            headA = headA.next
            headB = headB.next
        return None
