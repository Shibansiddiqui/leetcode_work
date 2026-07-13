class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        new_list = [0] * len(nums)
        new_list[0] = nums[0]
        for i in range(1,len(nums)):
            new_list[i] = new_list[i-1] + nums[i]

        return new_list
