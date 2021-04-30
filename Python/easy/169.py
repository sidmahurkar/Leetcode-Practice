from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        ans = 0
        frequency = floor(len(nums)/2)
        nums_count = Counter(nums)
        for element in nums_count:
            if nums_count[element] > frequency:
                return element
        