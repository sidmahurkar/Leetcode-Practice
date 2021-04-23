class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        
        ans = 0
        if n == 0:
            return start
        arr = [start + 2*i for i in range(n)]
        for i in arr:
            ans=ans^i
        
        return ans
        
        