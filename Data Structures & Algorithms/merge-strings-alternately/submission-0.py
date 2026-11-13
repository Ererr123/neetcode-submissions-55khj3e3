class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        if word1 is None or word2 is None:
            return ""
        new = ""

        n1, n2 = 0, 0

        while n1 < len(word1) and n2 < len(word2):
            new += (word1[n1])
            new += (word2[n2])
            n1 += 1
            n2 += 1

        while n1<len(word1):
             new += (word1[n1])
             n1 += 1
        
        while n2<len(word2):
             new += (word2[n2])
             n2 += 1
             
        return new