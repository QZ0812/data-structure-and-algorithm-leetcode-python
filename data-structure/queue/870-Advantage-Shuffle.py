# time O(n*logn)
# space 0(n)
import heapq
class Solution:
    def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        ans = [0  for _ in range(len(nums1))]
        hp = [(-num2, i) for i, num2 in enumerate(nums2)]
        heapq.heapify(hp)

        while nums1:
            num2, i = heapq.heappop(hp)
            if nums1[-1] > abs(num2):
                ans[i] = nums1[-1]
                nums1.pop()
            else:
                ans[i] = nums1[0]
                nums1.remove(nums1[0])
                
        return ans


from collections import deque
class Solution:
    def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
        A = deque(sorted(nums1))
        B = deque(sorted([(val, idx) for idx, val in enumerate(nums2)]))
        res = [0] * len(nums2)
        while B:
            val, idx = B.pop()
            res[idx] = A.pop() if A[-1] > val else A.popleft()
        return res
