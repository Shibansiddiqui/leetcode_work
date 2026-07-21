class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        # for i in range(n):
        #     for j in range(n-i-1):
        #         if nums[j] > nums[j+1]:
        #             nums[j], nums[j+1] = nums[j+1], nums[j]
        maxi = max(nums)
        mn = min(nums)
        freq_list = [0] * (maxi-mn+1) #creating correct storrange
        for i in nums:
            freq_list[i - mn] += 1 # using mn so we can avoid using negative indexes
        nums = []
        for j in range(len(freq_list)):
            while freq_list[j] > 0:
                nums.append(j + mn) # converting back to orignal indexes, by subracting from mn that we added earlier
                freq_list[j] -= 1

        return nums            