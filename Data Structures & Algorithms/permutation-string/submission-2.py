class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        size = len(s1)
        
        target = sorted(s1)
        left, right = 0, size

        while right <= len(s2):
            window = s2[left : right]
            if target == sorted(window):
                return True
            left += 1
            right += 1
            
        return False
