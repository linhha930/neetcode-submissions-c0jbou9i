class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        max_amt = 0

        while l < r:
            width = r - l
            area = min(heights[l], heights[r]) * width
            max_amt = max(max_amt, area)

            # move the shorter wall
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

        return max_amt