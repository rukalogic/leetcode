class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums = list(set(nums))
        n = len(nums)
        if n < 3:
            return max(nums)
        max_nums = set()
        for i in range(3):
            max_no = 0
            while max_no in max_nums:
                max_no += 1
            for j in range(n):
                if j in max_nums:
                    continue
                max_no = j if nums[j] > nums[max_no] else max_no
            if i == 2:
                return nums[max_no]
            max_nums.add(max_no)


        