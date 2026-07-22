class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # lst = []
        # ans = 0
        # for ch in s:
        #     while ch in lst:
        #         lst.pop(0)
        #     lst.append(ch)
        #     ans = max(ans, len(lst))
        # return ans
        longest = 0
        lst = [] 
        for i in range(len(s)):
            while s[i] in lst: 
                lst.pop(0)          
            lst.append(s[i]) 
            longest = max(longest,len(lst))
        return longest        