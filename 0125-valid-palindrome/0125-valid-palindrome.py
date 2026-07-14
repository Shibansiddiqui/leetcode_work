class Solution:
    def is_alpha_numeric(self,s):
            x = ord(s)
            if 48<=x<=57 or 65<=x<=90 or 97<=x<=122 :
                return True
            return False   
    def isPalindrome(self, s: str) -> bool:
         


        s = s.lower()
        l = 0
        r = len(s)-1

        while l < r :
            if not self.is_alpha_numeric(s[l]):
                l +=1

            elif not self.is_alpha_numeric(s[r]):
                r -=1
            elif s[l] == s[r]:
                l += 1
                r -=1
            else:
                return False  
        return True         