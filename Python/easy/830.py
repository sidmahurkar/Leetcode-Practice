class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        
        s += " "
	length = 1
        start_idx = 0

        ans_list = []
        inter_list = []
        
        for i in range(1,len(s)):
            
            if (s[i-1] == s[i]):
                length += 1
            
            else:
                if length >= 3:
                    ans_list.append([start_idx,i-1])
                    
                start_idx = i
                length = 1
        
        return ans_list             
                    
                    
                
            
        