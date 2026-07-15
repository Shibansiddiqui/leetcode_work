class Solution:
    def firstUniqChar(self, s: str) -> int:
        hashm = {}
        for ch in s:
            if ch not in hashm:
                hashm[ch] = 1
            else:
                hashm[ch] += 1     
        for i in hashm:
            if hashm[i] == 1:
                return s.index(i)
        return -1