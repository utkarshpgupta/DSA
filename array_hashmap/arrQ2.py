class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        word1 = list(s)
        word2 = list(t)

        word1.sort()
        word2.sort()

        if(word1 == word2):
            return True
        else:    
            return False