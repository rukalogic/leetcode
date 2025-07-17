class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        result = [1] * n  # Initialize result array with 1s

        # Step 1: Calculate prefix products
        left = 1
        for i in range(n):
            result[i] = left
            left *= nums[i]

        # Step 2: Calculate suffix products and multiply with prefix
        right = 1
        for i in reversed(range(n)):
            result[i] *= right
            right *= nums[i]

        return result
