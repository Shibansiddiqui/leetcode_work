class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
       h_map = {}
       for i,num in enumerate(nums):
        find = target - num
        if find not in h_map:
            h_map[num] = i

        else:
            index = h_map[find]
            return [index,i]