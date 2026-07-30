class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Create pairs of (value, original_index) to preserve indices after sorting
        indexed_nums = sorted((val, i) for i, val in enumerate(nums))
        
        j = len(indexed_nums) - 1
        i = 0

        while i < j:
            current_sum = indexed_nums[i][0] + indexed_nums[j][0]
            if current_sum == target:
                res = [indexed_nums[i][1], indexed_nums[j][1]]
                res.sort()
                return res
            elif current_sum > target:
                j -= 1
            else:
                i += 1
        
        return []