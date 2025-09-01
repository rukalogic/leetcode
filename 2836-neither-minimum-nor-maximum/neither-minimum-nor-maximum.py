class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if i == 0:
                minm = nums[i]
            minm = min(minm, nums[i])
        for i in range(len(nums)):
            if i == 0:
                maxi = nums[i]
            maxi = max(maxi, nums[i])
        for num in nums:
            if num != maxi and num != minm:
                return num
        return -1

        