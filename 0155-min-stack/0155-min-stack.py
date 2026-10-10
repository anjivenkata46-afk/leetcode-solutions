class MinStack(object):

    def __init__(self):
        # Main stack to store all elements
        self.stack = []
        # Auxiliary stack to keep track of the minimum elements
        self.min_stack = []

    def push(self, val):
        """:type val: int
        :rtype: None
        """
        self.stack.append(val)
        # If min_stack is empty or the new value is less than or equal 
        # to the current minimum, push it onto min_stack as well.
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self):
        """:rtype: None
        """
        # If the popped element is the current minimum, remove it from min_stack too.
        if self.stack.pop() == self.min_stack[-1]:
            self.min_stack.pop()

    def top(self):
        """:rtype: int
        """
        return self.stack[-1]

    def getMin(self):
        """:rtype: int
        """
        return self.min_stack[-1]