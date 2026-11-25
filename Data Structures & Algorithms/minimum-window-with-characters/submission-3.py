class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s)< len(t):
            return ""
        if t =="":
            return ""

        minLength = len(s)

        if minLength == len(t) and sorted(s)==t:
            return s
        
        ans = ""
        charCount = {}
        res = len(s)
        for i in t:
            charCount[i] = charCount.get(i,0)+1

        l = 0
        for r in range(len(s)):
            if s[r] in charCount:
                charCount[s[r]]-=1

            while (max(charCount.values()) == 0):
                substr=s[l:r+1]
                if r-l+1<=minLength:
                    ans = substr
                    minLength =r-l+1 

                if s[l] in charCount:
                    charCount[s[l]]+=1 
                l+=1

        return ans