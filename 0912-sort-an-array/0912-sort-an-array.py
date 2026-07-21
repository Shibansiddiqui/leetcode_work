class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        # for i in range(n):
        #     for j in range(n-i-1):
        #         if nums[j] > nums[j+1]:
        #             nums[j], nums[j+1] = nums[j+1], nums[j]
        maxi = max(nums)
        mn = min(nums)
        freq_list = [0] * (maxi-mn+1)
        for i in nums:
            freq_list[i - mn] += 1
        nums = []
        for j in range(len(freq_list)):
            while freq_list[j] > 0:
                nums.append(j + mn)
                freq_list[j] -= 1

        return nums            