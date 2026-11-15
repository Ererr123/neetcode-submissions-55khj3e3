class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        area = 0
        for i in range(len(heights)):
            current = (r - l) * min(heights[l], heights[r])
            area = max(area, current)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return area