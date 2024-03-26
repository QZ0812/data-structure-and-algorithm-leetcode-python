# time   O(n * log(n))
# space  O(n*k)


import heapq
class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        q = [1]
        heapq.heapify(q)
        for i in range(n):
            p = heapq.heappop(q)
            for prime in primes:
                heapq.heappush(q, p*prime)
                if p%prime == 0:
                    break
        
        return p
