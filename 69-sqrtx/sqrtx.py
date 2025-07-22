class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x 
        sqrt = x/2      
        while True:
            sqrt = (sqrt+ x/sqrt)/2
            int_sqrt = int(sqrt)
            if int_sqrt * int_sqrt <= x < (int_sqrt + 1) * (int_sqrt + 1):
                return int_sqrt

        