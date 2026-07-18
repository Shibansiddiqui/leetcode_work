class Solution:
    def largestOddNumber(self, num: str) -> str:
        
        while len(num) > 0:
            last_digit = int(num[-1])

            if last_digit % 2 != 0:
                return num

            num = num[:-1]

        return ""