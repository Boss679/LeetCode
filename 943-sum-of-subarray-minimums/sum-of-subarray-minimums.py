class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(arr)
        dp = [0] * n
        stack, res = [], 0

        for i in range(n):
            while stack and arr[stack[-1]] > arr[i]:
                stack.pop()
            
            j = stack[-1] if stack else -1
            dp[i] = (dp[j] if j != -1 else 0) + arr[i] * (i - j)
            dp[i] %= MOD
            res = (res + dp[i]) % MOD
            stack.append(i)

        return res