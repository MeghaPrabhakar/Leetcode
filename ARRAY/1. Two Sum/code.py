#https://leetcode.com/problems/two-sum/
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map={}
        for i,num in enumerate(nums):
            diff=target - num
            if(diff in num_map):
                return [i,num_map[diff]]
            num_map[num]=i
        return None
