class Solution:
    def partitionString(self, s: str) -> int:
        curSet = set()
        res = 1
        for c in s:
            if c in curSet:
                res += 1
                curSet.clear()
            curSet.add(c)
        return res