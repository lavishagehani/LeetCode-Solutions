class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        count = 0
        s = s.rstrip()
        for i in range(len(s)-1, -1, -1):
            if s[i].isalpha():
                count += 1
                continue
            if s[i].isspace():
                break  
        return count  