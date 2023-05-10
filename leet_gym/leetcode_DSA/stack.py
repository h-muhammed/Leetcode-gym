class Solution:
    def isValid(self, s: str) -> bool:
        """

        """
        stack = []
        for item in s:
            if item == '(' or item == '{' or item == '[':
                stack.append(item)
            else:
                if not stack:
                    return False
                elif item == ')' and stack[-1] == '(':
                    stack.pop()
                elif item == '}' and stack[-1] == '{':
                    stack.pop()
                elif item == ']' and stack[-1] == '[':
                    stack.pop()
                else: return False
                
                
        return not stack

            
