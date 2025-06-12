# Problem: Fair Distribution of Cookies - https://leetcode.com/problems/fair-distribution-of-cookies/

class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        l = [0]*k 
        self.s = float('inf')
        def seri(l,i):
            if i>=len(cookies):
                self.s = min(self.s,max(l))
                return 
            if max(l)>=self.s:
                return 
            for j in range(k):
                l[j]+=cookies[i]
                seri(l,i+1)
                l[j]-=cookies[i]
        
        seri(l,0)
        return self.s