# Problem: Last Stone Weight - https://leetcode.com/problems/last-stone-weight/

import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones)==1:
            return stones[0]
        stones = [-stone for stone in stones]  
        heapq.heapify(stones)

        while len(stones) > 1:
            y = -heapq.heappop(stones)
            x = -heapq.heappop(stones)
            if y != x:
                new=y-x
                heapq.heappush(stones, -new)

        return -stones[0] if stones else 0