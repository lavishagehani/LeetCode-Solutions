class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = s.replace(" ", "")
        s = re.sub(r"[^a-z0-9]", "", s)
        new = ""
        for i in range(len(s)-1, -1, -1):
            new += s[i]
        if new == s:
            return True
        return False