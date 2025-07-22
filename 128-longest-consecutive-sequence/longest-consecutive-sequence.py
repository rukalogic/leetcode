class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        refined_list = set(nums)
        lenght: int = 0
        longseq = 0
        for item in refined_list:
            if item - 1 not in refined_list:
                lenght = 0
                while item + lenght in refined_list:
                    lenght += 1
            longseq = max(longseq, lenght)
        return longseq
            
