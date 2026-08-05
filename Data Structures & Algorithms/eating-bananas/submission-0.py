class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        piles_len = len(piles)
        m = max(piles)      # longest number's length
        right = m
        left = 1
        min_k = m

        while left <= right:
            mid = (left + right) // 2
            time = 0
            for pile in piles:
                time += (pile + mid - 1) // mid

            if time <= h:
                min_k = mid
                right = mid - 1
            else:
                left = mid + 1

        return min_k