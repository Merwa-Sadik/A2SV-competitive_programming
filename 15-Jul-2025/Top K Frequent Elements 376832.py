# Problem: Top K Frequent Elements - https://leetcode.com/problems/top-k-frequent-elements/

from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
      
        count = defaultdict(int)
        for num in nums:
            count[num] += 1
        heap  = []
        for num, cnt in count.items():
            heapq.heappush(heap, [cnt, num])
            if len(heap) > k:
                heapq.heappop(heap)
        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res
