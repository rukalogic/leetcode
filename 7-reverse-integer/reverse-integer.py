class Solution:
    def reverse(self, x: int) -> int:
        x1 = str(abs(x))
        if x < 0:
            ans = int('-' +x1[::-1])
            if ans > 2**31 -1 or ans< -2**31:
                return 0
            else:
                return ans
        else:
            ans = int(x1[::-1])
            if ans > 2**31 -1 or ans< -2**31:
                return 0
            else:
                return ans

        