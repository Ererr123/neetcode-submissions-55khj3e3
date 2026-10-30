from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
    
        frequencies = Counter(nums)

        return  max(frequencies, key=frequencies.get)