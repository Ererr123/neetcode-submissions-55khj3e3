class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
            
        for i, characters in enumerate(zip(*strs)):
            if len(set(characters)) > 1:
                return strs[0][:i]
                
        return min(strs, key=len)