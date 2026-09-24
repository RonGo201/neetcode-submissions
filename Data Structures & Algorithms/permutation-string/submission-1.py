class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1_counts, s2_counts = [0] * 26, [0] * 26
        for c in s1:
            s1_counts[ord(c) - ord('a')] += 1

        l, r = 0, len(s1) - 1
        for i in range(len(s1)):
            s2_counts[ord(s2[i]) - ord('a')] += 1

        if s1_counts == s2_counts:
                return True

        while r < len(s2) - 1:
            s2_counts[ord(s2[l]) - ord('a')] -= 1
            r += 1
            l += 1
            s2_counts[ord(s2[r]) - ord('a')] += 1
            if s1_counts == s2_counts:
                return True

        return False