class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
       index_map = {}
       for i,num in enumerate(nums):
        find = target - num
        if find not in index_map:
            index_map[num] = i

        else:
            index = index_map[find]
            return [index,i]