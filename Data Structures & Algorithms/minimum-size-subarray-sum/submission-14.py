class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        size = len(nums)

        if sum(nums) < target:
            return 0

        left = 0
        current = size
        window_sum = 0

        for right in range(size):
            window_sum += nums[right]

            while window_sum >= target:
                current = min(current, right - left + 1)
                window_sum -= nums[left]
                left += 1

        return current