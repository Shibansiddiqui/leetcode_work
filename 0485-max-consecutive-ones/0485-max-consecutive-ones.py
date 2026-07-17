class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        longest = 0
        lst = [] 
        for i in nums: 
                if i !=1:
                    lst.clear()    
                elif i == 1:
                    lst.append(i)     
                longest = max(longest,len(lst))
                
        return longest