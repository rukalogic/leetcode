class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        setform = {}
        for i in range(len(nums)):
            setform[nums[i]] = i
        return nums != list(setform.keys())


        
        