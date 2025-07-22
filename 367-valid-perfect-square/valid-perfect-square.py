class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num < 2:
            return True
        sqrt = num // 2
        while True:
            new_sqrt = (sqrt + num / sqrt) /2
            if abs(new_sqrt - sqrt) < 1e-6:
                break
            sqrt = new_sqrt
        return int(sqrt) * int(sqrt) == num
            