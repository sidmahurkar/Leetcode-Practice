from collections import Counter


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        ans = True
        
        ransom_counter = Counter(ransomNote)
        magazine_counter = Counter(magazine)
        
        for char in ransom_counter:
            if((ransom_counter[char]>magazine_counter[char]) or (char not in magazine)):
                ans = False
                break
                
        return ans
        