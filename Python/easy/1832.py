class Solution(object):
    def checkIfPangram(self, sentence):
    
        for i in sentence:
            a.append(i)
        a = set(a)
        if(len(a) == 26):
            return True
        else:
            return False
        
        
        """
        :type sentence: str
        :rtype: bool
        """
        