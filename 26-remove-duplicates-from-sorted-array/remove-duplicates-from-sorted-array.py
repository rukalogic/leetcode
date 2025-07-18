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
        for i in range(len(nums) - 1, -1, -1):
            if not isinstance(nums[i], int):
                nums.pop(i)

        return no_of_unique