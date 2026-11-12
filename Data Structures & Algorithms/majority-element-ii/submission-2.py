class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        """count = defaultdict(int)

        for n in nums:
            count[n] += 1

            if len(count) <= 2:
                continue
            new_count = defaultdict(int)
            for n, c in count.items():
               if c > 1:
                new_count[n] = c - 1
            count = new_count
        
        res = []
        for n in count:
            if nums.count(n) > len(nums) // 3:
                res.append(n)
        return res"""

        candidate1 = candidate2 = None
        count1 = count2 = 0

        for num in nums:
            if num == candidate1:
                count1 += 1
            elif num == candidate2:
                count2 += 1
            elif count1 == 0:
                candidate1 = num
                count1 = 1
            elif count2 == 0:
                candidate2 = num
                count2 = 1
            else:
                count1 -= 1
                count2 -= 1

        result = []
        for candidate in (candidate1, candidate2):
            if candidate is not None and nums.count(candidate) > len(nums) // 3:
                if candidate not in result:
                    result.append(candidate)

        return result


