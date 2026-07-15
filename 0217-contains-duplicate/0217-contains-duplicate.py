class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        mapn = {}
        for num in nums:
            if num not in mapn:
                mapn[num] = 1
            else:
                return True
        return False        