class Solution(object):
    def calculate(self, s):
        """:type s: str
        :rtype: int
        """
        stack = []
        current_number = 0
        last_operator = '+'
        n = len(s)
        
        for i in range(n):
            char = s[i]
            
            if char.isdigit():
                current_number = current_number * 10 + int(char)
                
            # If it's an operator or the last character in the string
            if (not char.isdigit() and char != ' ') or i == n - 1:
                if last_operator == '+':
                    stack.append(current_number)
                elif last_operator == '-':
                    stack.append(-current_number)
                elif last_operator == '*':
                    stack.append(stack.pop() * current_number)
                elif last_operator == '/':
                    # Python's // floors towards negative infinity, so use int() to truncate towards zero
                    top_element = stack.pop()
                    if top_element < 0:
                        stack.append(-((-top_element) // current_number))
                    else:
                        stack.append(top_element // current_number)
                        
                last_operator = char
                current_number = 0
                
        return sum(stack)
        