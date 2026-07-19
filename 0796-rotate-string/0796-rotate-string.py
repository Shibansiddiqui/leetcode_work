class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        n = len(s)
        ss = 2 * s 
        for i in range(n):
            curr = ss[i:i+n]
            print(curr)
            if goal == curr:
                return True
        return False    
        #  return len(s) == len(goal) and goal in (s + s)