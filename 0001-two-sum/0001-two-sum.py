class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
       map = {}
       for i,num in enumerate(nums):
        find = target - num
        if find not in map:
            map[num] = i

        else:
            index = map[find]
            return [i,index]