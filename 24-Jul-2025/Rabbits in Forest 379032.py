# Problem: Rabbits in Forest - https://leetcode.com/problems/rabbits-in-forest/

from collections import Counter

class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        counts = Counter(answers)
        total = 0
        
        for k, v in counts.items():
            group_size = k + 1
            num_groups = v // group_size
            if v % group_size != 0:
                num_groups += 1
            total += num_groups * group_size
        
        return total
