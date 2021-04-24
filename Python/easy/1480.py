class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        
        ans = []
        summ = 0
        for i in nums:
            summ += i 
            ans.append(summ)
            
        return ans
            