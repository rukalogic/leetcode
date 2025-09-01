class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if i == 0:
                minm = nums[i]
                maxi = nums[i]
            minm = minm if minm < nums[i] else nums[i]
            maxi = maxi if maxi > nums[i] else nums[i]
        for num in nums:
            if num != maxi and num != minm:
                return num
        return -1

        