class Solution:
    def lower_bound(self,arr, target):
        left = 0
        right = len(arr) - 1
        ans = len(arr)

        while left <= right:
            mid = (left + right) // 2

            if arr[mid] >= target:
                ans = mid
                right = mid - 1
            else:
                left = mid + 1

        return ans
    def searchInsert(self, nums: List[int], target: int) -> int:
        return self.lower_bound(nums,target)
        

    
    