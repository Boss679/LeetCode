class Solution:
    def minOperations(self, nums: List[int]) -> int:
        N = len(nums)
        res = float("inf")
        nums = sorted(set(nums))
        n = len(nums)

        for i in range(n):
            l, r = i, n
            while l < r:
                mid = (l + r) // 2
                if nums[mid] < nums[i] + N:
                    l = mid + 1
                else:
                    r = mid
            noChange = l - i
            res = min(res, N - noChange)

        return res