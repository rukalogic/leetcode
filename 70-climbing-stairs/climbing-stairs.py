from functools import lru_cache
class Solution:
    @classmethod
    @lru_cache(maxsize=None)
    def climbStairs(cls, n: int) -> int:
        if n == 1:
            return 1
        elif n ==2:
            return 2
        else:
            return Solution.climbStairs(n-1)+Solution.climbStairs(n-2)
        