class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if len(nums) < k:
            return []
        

        max_window = []
        q = deque()  # stores indices

        for i, num in enumerate(nums):
            # Remove indices that are out of the current window
            if q and q[0] < i - k + 1:
                q.popleft()
            
            # Maintain decreasing order in deque
            while q and nums[q[-1]] < num:
                q.pop()
            
            q.append(i)
            
            # Window is fully formed
            if i >= k - 1:
                max_window.append(nums[q[0]])
        
        return max_window