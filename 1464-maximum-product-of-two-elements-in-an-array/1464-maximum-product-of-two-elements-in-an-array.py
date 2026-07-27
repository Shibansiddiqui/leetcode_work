class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        largest = largest_2 = float("-inf")
        # maxi = 0
        for num in nums:
            if num > largest:
                largest_2 = largest
                largest = num

            elif num > largest_2:
                largest_2 = num

        # maxi = max(maxi,(largest-1)*(largest_2-1))

        # return maxi   
        return (largest-1)*(largest_2-1) 