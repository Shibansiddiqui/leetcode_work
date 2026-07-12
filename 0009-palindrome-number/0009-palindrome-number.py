class Solution:
    def isPalindrome(self, x: int) -> bool:
        # x = str(x)
        # if x == x[::-1]:
        #     return True
        # else:
        #     return False     

        num = x
        result = 0
        while num > 0:
            l_d = num%10
            result = result*10 + l_d
            num = num//10
        return result == x    