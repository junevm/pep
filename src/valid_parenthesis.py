def is_valid_parentheses(s: str) :
    stack = []
    mapping = {')': '(', ']': '[', '}': '{'}
    
    for char in s:
        if char in mapping:
            top_element = stack.pop() if stack else '#'
            if mapping[char] != top_element:
                return False
        elif char in mapping.values():
            stack.append(char)
    
    return not stack

print(is_valid_parentheses("()[]{}"))  
