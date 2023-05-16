class MinStack:

    def __init__(self):
        self._stack = []
        self._min_stack = []

    def push(self, val: int) -> None:
        self._stack.append(val)
        current_min = val
        if len(self._min_stack) > 0:
            current_min = min(self.getMin(), val)
        self._min_stack.append(current_min)

    def pop(self) -> None:
        self._stack.pop()
        self._min_stack.pop()

    def top(self) -> int:
        if len(self._stack) > 0:
            return self._stack[-1]

    def getMin(self) -> int: # noqa
        if len(self._min_stack) > 0:
            return self._min_stack[-1]
