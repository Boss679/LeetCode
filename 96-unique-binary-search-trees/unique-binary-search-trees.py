class Solution:
    def numTrees(self, n: int) -> int:
        res = 1
        for i in range(1, n):
            res *= (n + i + 1)
            res //= i
        return res // n