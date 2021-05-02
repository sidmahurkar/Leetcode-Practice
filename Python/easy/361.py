from collections import Counter

class Solution:
    def findLucky(self, arr: List[int]) -> int:
        
        max_lucky = -1
        nums_count = Counter(arr)
        
        for num, count in nums_count.items():
            if num == count:
                max_lucky = max(max_lucky, num)
                
        return max_lucky
            