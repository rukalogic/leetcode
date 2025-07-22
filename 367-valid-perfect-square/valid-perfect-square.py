class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num < 2:
            return True
        left, right = 1, num//2
    
        while left <= right:
            mid = (right+left) // 2
            guess = mid * mid
            if guess == num:
                return True
            elif guess < num:
                left = mid + 1
            else:
                right = mid -1
        return False




            