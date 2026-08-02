class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        numsLen = len(nums)
        prefix = [0] * numsLen
        suffix = [0] * numsLen
        prefix[0] = nums[0]
        suffix[-1] = nums[-1]
        
        for i in range(1, numsLen):
            prefix[i] = nums[i] * prefix[i - 1]
            suffix[numsLen - 1 - i] = nums[numsLen - 1 - i] * suffix[numsLen - i]
        
        res = [0] * numsLen
        res[0] = suffix[1]
        res[numsLen - 1] = prefix[numsLen - 2]

        for i in range(1, numsLen - 1):
            res[i] = prefix[i - 1] * suffix[i + 1]
        
        return res

