# Problem: Minimum Moves to Reach Target Score - https://leetcode.com/problems/minimum-moves-to-reach-target-score/

class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        res = 0
        while target > 1:
            if maxDoubles > 0:
                if target % 2 == 0:
                    maxDoubles -= 1
                    target //=2
                    res += 1
                else:
                    target -= 1
                    res += 1
            else:
                return res + target - 1
        return res


        