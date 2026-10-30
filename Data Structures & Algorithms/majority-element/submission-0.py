from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
    
        frequencies = Counter(nums)

        return frequencies.most_common(1)[0][0]