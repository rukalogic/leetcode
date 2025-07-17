class Solution:
    def myAtoi(self, s: str) -> int:
        i = 0
        final = ''
        sign = 1
        n = len(s)
        if i == n:
                return 0
        while i<n and s[i]==' ':
            i +=1
        if i == n:
                return 0
        if s[i] == '-':
            sign = -1
            i+=1
            if i == n:
                return 0
        elif s[i] == '+':
            i+=1
            if i == n:
                return 0
        while s[i].isdigit() and i<n:
            final+=s[i]
            i+=1
            if i == n:
                break
        if final == '':
            return 0
        signed_final = sign*int(final)
        if signed_final > 2**31-1:
            return 2**31 -1
        elif signed_final < -2**31:
            return -2147483648
        else:
            return signed_final


        
        
           
        


            