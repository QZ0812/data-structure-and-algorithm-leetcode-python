# Time Complexity: O(nlogk) -- n number of all nodes, k lenth of lists
# Space Complexity: O(n)

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        
        while len(lists) > 1:
            merge = []
            for i in range(0, len(lists), 2):
                list1 = lists[i]
                list2 = lists[i+1] if i+1 < len(lists) else None
                merge.append(self.mergeTwoLists(list1, list2))
            lists = merge

        return lists[0]

    def mergeTwoLists(self, list1, list2):
        ans = dummy = ListNode(0)
        while list1 and list2:
            if list1.val >= list2.val:
                dummy.next = list2
                list2 = list2.next
            else:
                dummy.next = list1
                list1 = list1.next
            dummy = dummy.next

        dummy.next = list1 or list2
            
        return ans.next



# Time Complexity: O(nlogk) -- n number of all nodes, k lenth of lists
# Space Complexity: O(n)
from heapq import heapify, heappop, heappush
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists: 
            return None

        heap = [(ls.val, i, ls) for i, ls in enumerate(lists) if ls is not None ]

        heapify(heap)

        ans = dummy = ListNode(0)
        
        while heap:
            _, index , node = heappop(heap)
            if node.next:
                heappush(heap, (node.next.val, index, node.next))
            dummy.next = node
            dummy = dummy.next
            
        return ans.next
