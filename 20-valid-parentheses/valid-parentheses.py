class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        for i in s:
            if i in ["(","{","["]:
                stack.append(i) 
            else: 
                if not stack:
                    return False  
                if stack[-1] == "(" and i == ")":
                    stack.pop()
                    continue
                if stack[-1] == "{" in stack and i == "}":
                    stack.pop()
                    continue
                if stack[-1] == "[" in stack and i == "]":
                    stack.pop()
                    continue
                return False
        if stack:
            return False
        return True
        