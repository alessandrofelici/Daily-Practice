import math

class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []

        for token in tokens:
            try:
                # number case
                num = int(token)
                stack.append(num)
            except ValueError:
                # operator case
                match token:
                  case '+':
                        stack.append(stack[-2] + stack[-1])
                  case '-':
                        stack.append(stack[-2] - stack[-1])
                  case '*':
                        stack.append(stack[-2] * stack[-1])
                  case '/':
                        quotient = stack[-2] / stack[-1]
                        if quotient > 0:
                          stack.append(math.floor(quotient))
                        else:
                          stack.append(math.ceil(quotient))
                stack.pop(-2)
                stack.pop(-2)
        
        return stack[-1]
    
sol = Solution()
output = sol.evalRPN(["1","2","+","3","*","4","-"])
print(output)
output = sol.evalRPN(["4","13","5","/","+"])
print(output)
