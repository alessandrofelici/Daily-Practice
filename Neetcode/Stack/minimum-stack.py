class MinStack:

  def __init__(self):
    self.stack = []
    self.minStack = []

  def push(self, val: int) -> None:
    self.stack.append(val)
    val = min()
    # Case 1: first value
    if len(self.stack) is 1:
      self.minStack.append(val)
    # Case 2: existing values (compare)
    else:
      if val < self.minStack[-1]:
        self.minStack.append(val)
      else:
        self.minStack.append(self.minStack[-1])

  def pop(self) -> None:
    self.stack.pop()
    self.minStack.pop()

  def top(self) -> int:
    return self.stack[-1]

  def getMin(self) -> int:
    return self.minStack[-1]
