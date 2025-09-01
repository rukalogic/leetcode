class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        minm = min(nums)
        maxi = max(nums)
        for num in nums:
            if num != maxi and num != minm:
                return num
        return -1

        