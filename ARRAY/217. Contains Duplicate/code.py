class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen={}
        for i in range(len(nums)):
            if nums[i] in seen:
                return True
            seen[nums[i]]=1           
        return False

#class Solution:
#    def containsDuplicate(self, nums: List[int]) -> bool:
#        return len(nums) != len(set(nums))        
            
