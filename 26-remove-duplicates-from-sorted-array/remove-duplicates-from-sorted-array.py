class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        current = None
        no_of_unique = 0
        for i in range(len(nums)):
            if nums[i] == current:
                nums[i] = 0
            else:
                current = nums[i]
                no_of_unique += 1
                nums[no_of_unique-1] = nums[i]
        return no_of_unique