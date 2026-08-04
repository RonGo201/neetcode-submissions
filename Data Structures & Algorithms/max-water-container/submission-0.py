class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        max_cap = 0

        while l < r:
            cur_cap = (r - l) * min(heights[l], heights[r])
            if cur_cap > max_cap:
                max_cap = cur_cap
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        
        return max_cap