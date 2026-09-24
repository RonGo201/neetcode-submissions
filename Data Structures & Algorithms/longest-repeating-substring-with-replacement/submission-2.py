class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, max_freq, res = 0, 0, 0
        count = {}

        for r in range(len(s)):
            count[s[r]] = count.get(s[r], 0) + 1
            max_freq = max(max_freq, count[s[r]])

            curLen = r - l + 1
            if curLen - max_freq > k:
                count[s[l]] -= 1
                l += 1
            else:
                res = max(res, curLen)
        
        return res