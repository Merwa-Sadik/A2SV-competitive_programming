# Problem: Non-overlapping Intervals - https://leetcode.com/problems/non-overlapping-intervals/description/

from typing import List

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        res = 0

        def sort_by_end(interval):
            return interval[1]

        intervals.sort(key=sort_by_end)
        prev_end = intervals[0][1]
        for i in range(1, len(intervals)):
            if prev_end > intervals[i][0]:
                res += 1
            else:
                prev_end = intervals[i][1]
        return res
