class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        window_size = len(s1)
        if window_size > len(s2):
            return False
        
        s1_counts, s2_counts = [0] * 26, [0] * 26
        for i in range(window_size):
            s1_counts[ord(s1[i]) - ord('a')] += 1
            s2_counts[ord(s2[i]) - ord('a')] += 1

        if s1_counts == s2_counts: return True

        for i in range(window_size, len(s2)):
            s2_counts[ord(s2[i]) - ord('a')] += 1
            s2_counts[ord(s2[i - window_size]) - ord('a')] -= 1
            if s1_counts == s2_counts: return True

        return False