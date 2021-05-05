class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        
        def sorting_algo(logs):
            
            left_string, right_string = logs.split(" " ,1)
            
            if right_string[0].isalpha():
                return (0, right_string, left_string)
            
            else:
                return (1, )
            
        return sorted(logs, key = sorting_algo)
        