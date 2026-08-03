class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        max_len = 0
        for num in num_set:
            if num - 1 in num_set:
                continue

            counter = 1

            while num + 1 in num_set:
                counter += 1
                num = num + 1
            
            if counter > max_len:
                max_len = counter

        return max_len