# Problem: Largest Perimeter Triangle - https://leetcode.com/problems/largest-perimeter-triangle/

class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        
        indx = len(nums) - 1
        while indx >= 2:
            j = indx - 1
            if nums[j] + nums[j - 1] > nums[indx]:
                return nums[indx] + nums[j] + nums[j - 1]
            else:
                indx -= 1
        return 0