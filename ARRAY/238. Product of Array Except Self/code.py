#https://leetcode.com/problems/product-of-array-except-self/description/
##https://www.youtube.com/watch?v=cPM3_h4lt48&ab_channel=LitCode
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if not nums:
            return 0

        result = [1] * len(nums)

        prefix = 1
        for index in range(len(nums)):
            result[index] = prefix
            prefix *= nums[index]

        postfix = 1
        for index in range(len(nums)-1, -1, -1):
            result[index] *= postfix
            postfix *= nums[index]

        return result
        
