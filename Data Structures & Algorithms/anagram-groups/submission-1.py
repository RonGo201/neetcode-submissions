class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = {}
        
        for word in strs:
            char_count = [0] * 26  
            for char in word:
                index = ord(char) - ord('a')
                char_count[index] += 1

            dict_key = tuple(char_count)

            if dict_key not in anagram_map:
                anagram_map[dict_key] = []

            anagram_map[dict_key].append(word)

        return list(anagram_map.values())