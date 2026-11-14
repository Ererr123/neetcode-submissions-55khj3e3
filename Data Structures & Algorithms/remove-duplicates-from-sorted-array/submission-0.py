class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if nums is None:
            return 0
        
        k = 1

        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[k] = nums[i]
                k += 1
   
        return k


