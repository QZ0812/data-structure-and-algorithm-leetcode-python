# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# O(n) time and O(1) space
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return True
        # find middle point 
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        # reverse from middle point    
        pre = None
        while slow:
            temp = slow.next
            slow.next = pre
            pre = slow
            slow = temp
        # compare
        while pre:
            if pre.val != head.val:
                return False
            pre = pre.next
            head = head.next
        
        return True


# O(n) time and O(n) space
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        nums = []
        while head:
            nums.append(head.val)
            head = head.next
            
        l, r = 0, len(nums) - 1
        while l <= r:
            if nums[l] != nums[r]:
                return False
            l += 1
            r -= 1
            
        return True
