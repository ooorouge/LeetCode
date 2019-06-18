* No 20 Valid Parentheses
* use stack
* 如果栈是空的，入栈跳出循环？-> 如果匹配pop之后跳出循环-> 如果都不匹配继续入栈跳出循环
```python
class Solution:
    def isValid(self, s: str) -> bool:
        
        if not s:
            return True
        
        stack1 = []
        
        for item in s:
            
            if not stack1:
                stack1.append(item)
                continue
            
            if stack1[-1] == '(' and item == ')':
                stack1.pop()
                continue
            if stack1[-1] == '{' and item == '}':
                stack1.pop()
                continue
            if stack1[-1] == '[' and item == ']':
                stack1.pop()
                continue
                
            stack1.append(item)
                
                
        return (len(stack1) == 0)
```
