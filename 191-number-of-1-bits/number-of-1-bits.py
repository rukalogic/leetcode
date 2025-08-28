class Solution:
    def hammingWeight(self, n: int) -> int:
        no = 0
        while (n != 0):
            if n % 2 == 1:
                no += 1
            n //= 2
        return no
        