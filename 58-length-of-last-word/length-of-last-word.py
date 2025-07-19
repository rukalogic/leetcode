class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        clean = s.rstrip()
        lenght_of_last_word = 0
        for i in range(len(clean)-1, -1, -1):
            if clean[i] != ' ':
                lenght_of_last_word += 1
            else:
                return lenght_of_last_word
        return lenght_of_last_word


            
        