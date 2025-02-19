class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        def dfs(s):
            if len(s) == n:
                self.s += 1
                if self.s == k:
                    return s[:]
                return ""
            for i in ["a","b","c"]:
                if s[-1] == i: continue 
                x = dfs(s+i)
                if x: return x 
            return ""
        self.s = 0 
        for i in ["a","b","c"]:
            x = dfs(i)
            if x: return x 
        return ""

