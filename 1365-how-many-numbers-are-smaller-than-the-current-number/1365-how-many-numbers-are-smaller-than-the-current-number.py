class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        
        result = []
        for n in nums:
            start = 0
            for i in range(len(nums)):
                if n > nums[i]:
                    start += 1 
            result.append(start)

        return result    

        