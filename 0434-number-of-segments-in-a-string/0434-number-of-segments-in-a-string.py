class Solution:
    def countSegments(self, s: str) -> int:
       s = s.split()
       count = 0
       print(s)
       for i in s:
            if s != " ":
                count += 1
       return count       