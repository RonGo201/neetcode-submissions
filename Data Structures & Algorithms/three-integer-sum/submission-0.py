class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        sorted_nums = sorted(nums)
        nums_len = len(sorted_nums)
        for i in range(nums_len - 2):
            if i > 0 and sorted_nums[i] == sorted_nums[i - 1]:
                continue
            target = -sorted_nums[i]
            left, right = i + 1, nums_len - 1
            while left < right:
                new_sum = sorted_nums[left] + sorted_nums[right]
                if new_sum == target:
                    res.append([sorted_nums[i], sorted_nums[left], sorted_nums[right]])
                    while left < right and sorted_nums[left] == sorted_nums[left + 1]:
                        left += 1
                    left += 1
                elif new_sum < target:
                    left += 1
                else:
                    right -= 1
        
        return res
