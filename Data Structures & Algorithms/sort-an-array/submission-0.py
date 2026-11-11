class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(left, mid, right):
            n1 = mid - left + 1
            n2 = right - mid

            ## Create Temps
            L = [0] * n1
            R = [0] * n2

            ## Copy data to temp arrays L[] and R[]
            for i in range(n1):
                L[i] = nums[left + i]
            for j in range(n2):
                R[j] = nums[mid + 1 + j]
            
            i = 0
            j = 0
            k = left

            while i < n1 and j < n2:
                if L[i] <= R[j]:
                    nums[k] = L[i]
                    i += 1
                else:
                    nums[k] = R[j]
                    j += 1
                k += 1
            
            while i < n1:
                nums[k] = L[i]
                i += 1
                k += 1
            
            while j < n2:
                nums[k] = R[j]
                j += 1
                k += 1

        def mergeSort(left, right):
            if left >= right:
                return

            mid = (left + right) // 2

            mergeSort(left, mid)
            mergeSort(mid + 1, right)
            merge(left, mid, right)

        ## Kick off the merge sort on the entire array
        mergeSort(0, len(nums) - 1)

        return nums