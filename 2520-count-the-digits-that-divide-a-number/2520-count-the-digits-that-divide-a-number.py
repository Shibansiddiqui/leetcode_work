class Solution:
    def countDigits(self, num: int) -> int:

        nums = num
        count = 0
        while nums > 0:
            l_d = nums%10 
            if num%l_d == 0 and l_d != 0:
                count += 1
            nums = nums//10

        return count       


