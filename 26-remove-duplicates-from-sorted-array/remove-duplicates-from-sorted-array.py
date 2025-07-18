class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        current = None
        no_of_unique = 0
        for i in range(len(nums)):
            if nums[i] == current:
                nums[i] = '-'
            else:
                current = nums[i]
                no_of_unique += 1
        nums[:] = [x for x in nums if isinstance(x, int)]
        return no_of_unique