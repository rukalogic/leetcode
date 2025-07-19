class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a_dec = 0
        b_dec = 0
        answer =''
        for i in range(len(a)):
            a_dec += int(a[i])
            if i != len(a)-1:
                a_dec *= 2
        for i in range(len(b)):
            b_dec += int(b[i])
            if i != len(b)-1:
                b_dec *= 2
        sum = a_dec + b_dec
        while sum > 0:
             answer = str(sum%2) + answer
             sum //= 2
        if not answer:
            answer = '0'
        return answer 
