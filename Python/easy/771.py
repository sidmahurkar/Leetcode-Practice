class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        
        if len(jewels)==0 or len(stones)==0:
            return 0
        ans = 0
        jew = set(jewels)
        for i in jew:
            ans+= stones.count(i)
        return ans
            
            
        
        