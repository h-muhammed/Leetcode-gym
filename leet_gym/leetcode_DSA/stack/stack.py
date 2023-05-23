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

            
class Solution:
    def makeGood(self, s: str) -> str:
        """itype: str
        rtype: str
        return a string after operating the given
        instruction for a given string.
        """
        stack = []
        for idx in range(len(s)):
            if not stack:
                stack.append(s[idx])
                continue
            if(stack[-1].isupper() and stack[-1].lower() == s[idx]) or (stack[-1].islower() and stack[-1].upper() == s[idx]):
                stack.pop()
                continue
            stack.append(s[idx])
        return "".join(stack)