class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        res = []

        def dfs(num):
            if num > high:
                return
            if low <= num <= high:
                res.append(num)
            last_digit = num % 10
            if last_digit < 9:
                dfs(num * 10 + (last_digit + 1))

        for i in range(1, 10):
            dfs(i)

        return sorted(res)