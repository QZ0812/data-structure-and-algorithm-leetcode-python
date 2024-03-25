#time O(n*n) space O(n)
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        lenth, ans = len(points), 0

        for i in range(lenth):
            j = i + 1
            count = {}
            while j < lenth:
                slope = self.get_slope(points[i], points[j])
                count[slope] = 2 if slope not in count else count[slope] + 1
                j += 1
            ans = max(ans, max(count.values()) if count else 1)
                
        return ans
            
    
    def get_slope(self, point1, point2):
        if point2[0] - point1[0] == 0:
            return float('inf')
        
        return (point2[1] - point1[1])/(point2[0] - point1[0])
