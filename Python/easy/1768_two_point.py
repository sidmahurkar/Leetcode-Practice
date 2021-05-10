class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        ans = ""
        word1_c = 0
        word2_c = 0
        
        while(word1_c < len(word1) or word2_c < len(word2)):
            
            if word1_c < len(word1):
                ans+= word1[word1_c]
                word1_c+=1
                
            if word2_c < len(word2):
                ans+= word2[word2_c]
                word2_c+=1
                
        return ans
            
                
            
        