class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        
        g.sort()
        s.sort()
        
        ans = 0
        child = 0
        cookie = 0
        
        while(child<=len(g)-1 and cookie<=len(s)-1):
            
            if (s[cookie]>=g[child]):
                ans+=1
                cookie+=1
                child+=1
            else:
                cookie+=1
                
        return ans