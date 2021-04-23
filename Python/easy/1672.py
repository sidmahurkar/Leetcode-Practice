class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        
        maxx = 0
        for row in accounts:
            summ = 0
            for column in row:
                summ+=column
            if summ > maxx:
                maxx = summ
        
        return maxx
                
                
        