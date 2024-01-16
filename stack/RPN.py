# 150. Evaluate Reverse Polish Notation

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        for n in tokens:
            if n == '+':
                b, a = stack.pop(), stack.pop()
                res = a + b
                stack.append(res)
            elif n == '-':
                b, a = stack.pop(), stack.pop()
                res = a - b
                stack.append(res)
            elif n == '/':
                b, a = stack.pop(), stack.pop()
                res = int(a/b)
                print(a,b, res)
                stack.append(res)
            elif n == '*':
                b, a = stack.pop(), stack.pop()
                res = b * a
                stack.append(res)
            else:
                stack.append(int(n))
        
        return stack[0]