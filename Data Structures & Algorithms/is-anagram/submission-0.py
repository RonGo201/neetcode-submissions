class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sLen = len(s)
        tLen = len(t)
        
        if sLen != tLen:
            return False
        
        sMap = {}
        tMap = {}

        for i in range(sLen):
            if s[i] in sMap:
                sMap[s[i]] += 1
            else:
                sMap[s[i]] = 1
            
            if t[i] in tMap:
                tMap[t[i]] += 1
            else:
                tMap[t[i]] = 1

        for char in sMap:
            if char not in tMap or sMap[char] != tMap[char]:
                return False
        
        return True