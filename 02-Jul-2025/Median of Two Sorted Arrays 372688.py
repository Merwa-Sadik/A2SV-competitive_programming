# Problem: Median of Two Sorted Arrays - https://leetcode.com/problems/median-of-two-sorted-arrays/

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged = nums1 + nums2
        merged.sort()
        n = len(merged)
    
        if n % 2 == 1:
           return float(merged[n // 2])
        else:
           return (merged[n // 2 - 1] + merged[n // 2]) / 2.0
        