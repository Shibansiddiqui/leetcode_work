class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        

        start = 1
        for i in range(2,len(nums)):
            if  len(nums) < 2:
                return nums
            if nums[start-1] != nums[i]:
                start += 1
                nums[start] = nums[i]

        return start+1   