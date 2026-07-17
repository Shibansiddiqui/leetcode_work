class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq = {}

        for i in nums:
            if i not in freq:
                freq[i] = 1
            else:
                freq[i] += 1
            
        max_freq = float("-inf")
        its_element = 0
        for key,value in freq.items():
             if value > max_freq:
                max_freq = value
                its_element = key
        return its_element        
