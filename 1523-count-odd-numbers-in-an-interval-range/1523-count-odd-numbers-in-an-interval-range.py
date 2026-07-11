class Solution:
    def countOdds(self, low: int, high: int) -> int:
        # l = 0
        # for i in range(low,high+1):
        #     if i % 2 == 1:
        #         l +=1

        # return l      
        
         return (high + 1) // 2 - low // 2
