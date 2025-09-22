"""Min stack.

Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
"""

# all operations constant time. Space O(n). Trick is to use a second stack to store mins


class Stack:
    def __init__(self):
        self.stack = []

        # mins[i] represents the min value if self.stack
        # were popped/truncated down to i elements
        self.mins = []

    def push(self, val: int):
        self.stack.append(val)
        if self.mins == []:
            self.mins.append(val)
        else:
            # min value of new stack is either the most recently
            # pushed or the current min, whichever is lower
            self.mins.append(min(val, self.mins[-1]))

    def pop(self):
        if self.stack == [] or self.mins == []:
            raise ValueError("Popping from empty stack")
        _ = self.mins.pop()
        return self.stack.pop()

    def top(self):
        return self.stack[-1]

    def getMin(self):
        return self.mins[-1]
