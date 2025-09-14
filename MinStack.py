import math


class MinStack:
    """
    思路， 其他的内容和原始的栈一致就行了， 维护一个最小值的stack。
    该stack每次push的时候和栈顶取小push， 这样保证， 每次pop后
    都是当前栈里面最小的。
    """

    def __init__(self):
        self.stack = []
        self.min_stack = [math.inf]

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.min_stack.append(min(val, self.min_stack[-1]))

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
