class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # if sorted(s) == sorted(t):
        #     return True
        # elif    sorted(s) != sorted :
        #     return False
        # else:
        #    return False    
        if len(s) != len(t):
            return False
        freq = {}
        for i in s:
            if i not in freq:
                freq[i] = 1
            else:
                freq[i] += 1   
        for i in t:
            if i not in freq:
                return False
            else:
                freq[i] -= 1

        for i in freq.values():
            if i > 0:
                return False
        return True         

