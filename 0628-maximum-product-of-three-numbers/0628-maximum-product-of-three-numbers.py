class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        largest = largest_2 = largest_3 = float("-inf")
        smallest = smallest_2 = float("inf")
        for num in nums:
            if num > largest:
                largest_3 = largest_2
                largest_2 = largest
                largest = num
                
            elif num > largest_2:
                largest_3 =  largest_2
                largest_2 = num
         
            elif num > largest_3:
                largest_3 = num         

            if num < smallest:
                smallest_2 = smallest
                smallest = num
            elif num < smallest_2:
                smallest_2 = num   

        return max((largest * largest_2 * largest_3),
                    (largest * smallest * smallest_2))

  