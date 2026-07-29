class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        maxn = max(nums)
        freq = [0] * (maxn + 1) 
       
        for num in nums: 
            freq[num] += 1
        k = 0
        print(freq)
        for i in range(maxn+1):
            while freq[i] > 0:
                nums[k] = i
                k += 1
                freq[i] -= 1
