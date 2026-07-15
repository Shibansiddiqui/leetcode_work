class Solution:
    
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # import math
        # new_list = []
        # for i in range(len(nums)):
        #     current_nums = nums.copy()
        #     current_nums.pop(i)
        #     val = math.prod(current_nums)
        #     new_list.append(val)
        # return new_list    
        final_list = []
        l = []
        r = []

        n = 1
        for i in nums:
            n *= i
            l.append(n)

        m = 1
        for j in reversed(nums):
            m *= j
            r.append(m)  
        r.reverse()       

        for x in range(len(nums)):
            if x == 0:
                val = r[x + 1]
            elif x == len(nums) - 1:
                val = l[x - 1]
            else:
                val = l[x - 1] * r[x + 1]

            final_list.append(val)
        return final_list

