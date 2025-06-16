# Problem: Splitting a String Into Descending Consecutive Values - https://leetcode.com/problems/splitting-a-string-into-descending-consecutive-values/

class Solution:
    def splitString(self, s: str) -> bool:

        def canSplit(startIndex, previousNumber):
            if startIndex == len(s):
                return True

            for endIndex in range(startIndex, len(s)):
                currentNumber = int(s[startIndex:endIndex + 1])

                if currentNumber + 1 == previousNumber:
                    if canSplit(endIndex + 1, currentNumber):
                        return True

            return False

        for i in range(1, len(s)):
            firstNumber = int(s[:i])
            if canSplit(i, firstNumber):
                return True

        return False
