class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        n = len(set(nums))
        if n < 3:
            return max(nums)
        return sorted(list(set(nums)), reverse = True)[2]
        