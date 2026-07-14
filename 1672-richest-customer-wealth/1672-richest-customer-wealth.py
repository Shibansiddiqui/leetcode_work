class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        value = 0
        for acount in accounts:
            value =max(sum(acount),value)
        return value