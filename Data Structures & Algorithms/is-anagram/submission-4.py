from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ## a = "".join(sorted(s))
        ## b = "".join(sorted(t))
        ## if(a==b):
        ##    return True
        ## return False
        if len(s) != len(t):
            return False
        
        count = [0] * 26
        a_code = ord('a')
        
        for i in range(len(s)):
            count[ord(s[i]) - a_code] += 1
            count[ord(t[i]) - a_code] -= 1
            
        return all(c == 0 for c in count)
        