from collections import deque

"""
This is the interface that allows for creating nested lists.
You should not implement it, or speculate about its implementation
"""


class NestedInteger:
   def isInteger(self) -> bool:
       """
       @return True if this NestedInteger holds a single integer, rather than a nested list.
       """

   def getInteger(self) -> int:
       """
       @return the single integer that this NestedInteger holds, if it holds a single integer
       Return None if this NestedInteger holds a nested list
       """

   def getList(self) -> [NestedInteger]:
       """
       @return the nested list that this NestedInteger holds, if it holds a nested list
       Return None if this NestedInteger holds a single integer
       """


class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.mylist = deque(nestedList)
        self.buffer = deque()

    def next(self) -> int:
        return self.buffer.popleft()

    def _process_node(self, node):
        if node.isInteger():
            self.buffer.append(node.getInteger())
        else:
            for x in node.getList():
                self._process_node(x)

    def hasNext(self) -> bool:
        if self.buffer:
            return True

        if not self.mylist:
            return False

        while self.mylist and not self.buffer:
            self._process_node(self.mylist.popleft())

        return len(self.buffer) > 0

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
