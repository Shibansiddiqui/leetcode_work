class Solution:
    def subtractProductAndSum(self, n: int) -> int:
            result_mul = 1
            result_add = 0
            num = n
            while num >0:
                l_d =  num%10
                result_mul *= l_d
                result_add += l_d
                num = num//10
            return (result_mul - result_add)   