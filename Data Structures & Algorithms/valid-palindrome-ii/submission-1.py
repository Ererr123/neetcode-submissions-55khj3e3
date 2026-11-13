class Solution:
    def validPalindrome(self, s: str) -> bool:
        """"if s is None:
            return None
        temp = ""
        for i in range(len(s)):
            temp = s[:i] + s[i+1:]
            if temp == temp[::-1]:
                return True
        return False"""

        left, right = 0, len(s) - 1
        
        while left < right:
            if s[left] != s[right]:
                skip_left = s[left + 1 : right + 1]
                skip_right = s[left : right]
                return skip_left == skip_left[::-1] or skip_right == skip_right[::-1]
            
            left += 1
            right -= 1
            
        return True