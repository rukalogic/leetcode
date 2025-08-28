class Solution:
    def isUgly(self, n: int) -> bool:
        me = [2, 3, 5]
        if n < 1:
            return False
        while n != 1:
            no = 0
            for item in me:
                if n % item == 0:
                    n //= item
                    no += 1
            if no == 0 and n != 1:
                return False
        return True
        