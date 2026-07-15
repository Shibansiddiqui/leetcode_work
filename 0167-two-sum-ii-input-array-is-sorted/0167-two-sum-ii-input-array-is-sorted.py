class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        l = 0
        r = n-1
        while l<r:
            current_sum = numbers[l]+numbers[r]
            if target == current_sum:
                return l+1, r+1
            elif target > current_sum:
                l += 1
            elif target < current_sum:
                r -=1     