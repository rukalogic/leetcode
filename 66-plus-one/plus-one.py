class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        answer = [0] * (len(digits) + 1)
        next_plus_one = True
        for i in range(len(digits)-1, -1, -1):
            if digits[i] == 9 and next_plus_one:
                answer[i+1] = 0
                next_plus_one = True
            elif next_plus_one:
                answer[i+1] = digits[i] +1
                next_plus_one = False
            else:
                answer[i+1] = digits[i]
        if next_plus_one:
            answer[0] = 1
        if answer[0]:
            return answer
        else:
            answer.pop(0)
            return answer


            


            