# 20. Valid Parentheses

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        stack = []
        brackets = {'(':')', '{':'}', '[':']'}
        for c in s:
            if c in brackets:
                stack.append(c)
            elif c in brackets.values():
                if stack and c == brackets[stack[-1]]:
                    stack.pop()
                else:
                    print('sad')
                    return False
        print(stack)
        print('yay')
        return not stack
        
sol = Solution()
s = "{()[]}"
sol.isValid(s)