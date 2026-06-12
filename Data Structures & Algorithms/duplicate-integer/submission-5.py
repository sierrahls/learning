class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        no_duplicates = set(nums) #creates a set of nums
        if len(set(nums)) < len(nums):
            return True
        else:
            return False