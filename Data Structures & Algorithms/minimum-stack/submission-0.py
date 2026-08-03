class MinStack:

    def __init__(self):
        self.st = []
        self.min_val = float('inf')

    def push(self, val: int) -> None:
        self.st.append((val, self.min_val))
        if val < self.min_val:
            self.min_val = val

    def pop(self) -> None:
        top_val, prev_min = self.st[-1]
        self.min_val = prev_min
        self.st.pop()


    def top(self) -> int:
        top_val, prev_min = self.st[-1]
        return top_val

    def getMin(self) -> int:
        return self.min_val
