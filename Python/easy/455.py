class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
         ans = 0
         g.sort()
         s.sort()
        
         for cookie in s:   
             for child in g:
                 if cookie >= child:
                     g.remove(child)
                     ans+=1
                     break
        
         return ans