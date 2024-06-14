#Solution Strategies:
#Two Pointers Approach:
#This technique involves iterating through both arrays using two pointers. By comparing the elements at the current pointers, we can merge the two arrays. Once merged, finding the median is straightforward.

#Binary Search Approach:
#Leveraging the properties of sorted arrays, we can apply a binary search on the smaller array, effectively partitioning both arrays. This method ensures we find the median without explicitly merging the arrays, adhering to the desired logarithmic time complexity.

#1. Two Pointers Merging Technique

  #The merging process traverses both arrays once, resulting in a time complexity of $$ O(m + n) $$, where $$ m $$ and $$ n $$ are the lengths of nums1 and nums2 respectively.
  #Space Complexity:  O(m + n)

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged = []
        i, j = 0, 0
        
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                merged.append(nums1[i])
                i += 1
            else:
                merged.append(nums2[j])
                j += 1
                
        while i < len(nums1):
            merged.append(nums1[i])
            i += 1
            
        while j < len(nums2):
            merged.append(nums2[j])
            j += 1
        
        mid = len(merged) // 2
        if len(merged) % 2 == 0:
            return (merged[mid-1] + merged[mid]) / 2
        else:
            return merged[mid]


#2. Binary Search with Partitioning
    # The algorithm performs a binary search on the smaller array, leading to a time complexity of $$ O(\log(\min(m, n))) $$. The algorithm uses only a constant amount of extra space, thus having a space complexity of $$ O(1) $$.

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        m, n = len(nums1), len(nums2)
        low, high = 0, m
        
        while low <= high:
            partitionX = (low + high) // 2
            partitionY = (m + n + 1) // 2 - partitionX
            
            maxX = float('-inf') if partitionX == 0 else nums1[partitionX - 1]
            maxY = float('-inf') if partitionY == 0 else nums2[partitionY - 1]
            minX = float('inf') if partitionX == m else nums1[partitionX]
            minY = float('inf') if partitionY == n else nums2[partitionY]
            
            if maxX <= minY and maxY <= minX:
                if (m + n) % 2 == 0:
                    return (max(maxX, maxY) + min(minX, minY)) / 2
                else:
                    return max(maxX, maxY)
            elif maxX > minY:
                high = partitionX - 1
            else:
                low = partitionX + 1
