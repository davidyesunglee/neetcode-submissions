class Solution:
    def maxArea(self, heights: List[int]) -> int:
        ans, r = 0, len(heights) - 1
        l = 0

        while l < r:
            area = min(heights[l], heights[r]) * (r - l)
            ans = max(ans, area)

            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1

        return ans