class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        
        start = 0
        if len(nums) <2:
            return nums
        for i in range(len(nums)):
            if nums[i]%2 ==0:
                nums[start], nums[i] = nums[i], nums[start]
                start += 1

        return nums        
