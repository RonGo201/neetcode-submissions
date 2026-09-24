class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r, res = 0, 0, 0
        window = set()
        counter = 0

        while l < len(s):
            if s[r] in window:
                window.remove(s[l])
                l += 1
                counter -= 1
            
            else:
                window.add(s[r])
                counter += 1
                if r < len(s) - 1:
                    r += 1
                if counter > res:
                    res = counter

        return res
            