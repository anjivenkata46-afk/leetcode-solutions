class MyQueue(object):

    def __init__(self):
        self.s1 = []
        self.s2 = []

    def push(self, x):
        """:type x: int
        :rtype: None
        """
        self.s1.append(x)

    def pop(self):
        """:rtype: int
        """
        self._move()
        return self.s2.pop()

    def peek(self):
        """:rtype: int
        """
        self._move()
        return self.s2[-1]

    def empty(self):
        """:rtype: bool
        """
        return not self.s1 and not self.s2

    def _move(self):
        # Helper method to transfer elements from s1 to s2 if s2 is empty
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())