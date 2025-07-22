class Solution:
    def mySqrt(self, x: int) -> int:
        sqrt = int(x / 2)
        while True:
            if sqrt == 0:
                return x
            sqrt = (sqrt+ x/sqrt)/2
            if int(sqrt) * int(sqrt) <= x < (int(sqrt) + 1) * (int(sqrt) + 1):
                return int(sqrt)

        