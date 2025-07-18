class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        current = None
        no_of_unique = 0
        for i in range(len(nums)):
            if nums[i] == current:
                nums[i] = 9999999999999999999999999999
            else:
                current = nums[i]
                no_of_unique += 1
        nums.sort()
        return no_of_unique



        