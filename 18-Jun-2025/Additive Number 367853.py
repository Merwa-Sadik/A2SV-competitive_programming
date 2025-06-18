# Problem: Additive Number - https://leetcode.com/problems/additive-number/

class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        n = len(num)
        for i in range(1, n):
            for j in range(i + 1, n):
                first = num[:i]
                second = num[i:j]
                if (len(first) > 1 and first[0] == '0') or (len(second) > 1 and second[0] == '0'):
                    continue

                a = int(first)
                b = int(second)
                rest = num[j:]
                while rest:
                    c = a + b
                    c_str = str(c)

                    if not rest.startswith(c_str):
                        break

                    rest = rest[len(c_str):]
                    a = b
                    b = c
                if rest == "":
                    return True

        return False
