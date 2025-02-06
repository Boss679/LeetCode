class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.stack = nestedList
        self.stack.reverse()

    def next(self) -> int:
        return self.stack.pop().getInteger()

    def hasNext(self) -> bool:
        while self.stack:
            top = self.stack[-1]
            if top.isInteger():
                return True
                
            self.stack.pop()
            self.stack.extend(reversed(top.getList()))
        return False