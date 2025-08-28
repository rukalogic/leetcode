class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        while n % 3 == 0:
            if n==0:
                return False
            if n/3 == n//3:
                n = n//3
            else:
                return False
            if n == 1:
                return True
        if n==1:
                return True
        return False
        