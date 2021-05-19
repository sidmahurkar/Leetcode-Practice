class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        
        count = 0
        
        for num in range(1,1001+k):
                            
            if num in arr:
                continue    
            else:
                count+=1
            
            if count == k:
                return num
            
        