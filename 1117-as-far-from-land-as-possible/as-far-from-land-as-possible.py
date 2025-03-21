class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        N, INF = len(grid), 10**6

        for r in range(N):
            for c in range(N):
                if grid[r][c] == 1:
                    continue
                grid[r][c] = INF
                if r > 0:
                    grid[r][c] = min(grid[r][c], grid[r - 1][c] + 1)
                if c > 0:
                    grid[r][c] = min(grid[r][c], grid[r][c - 1] + 1)

        res = 0
        for r in range(N - 1, -1, -1):
            for c in range(N - 1, -1, -1):
                if grid[r][c] == 1:
                    continue
                if r < N - 1:
                    grid[r][c] = min(grid[r][c], grid[r + 1][c] + 1)
                if c < N - 1:
                    grid[r][c] = min(grid[r][c], grid[r][c + 1] + 1)
                res = max(res, grid[r][c])

        return res - 1 if res < INF else -1