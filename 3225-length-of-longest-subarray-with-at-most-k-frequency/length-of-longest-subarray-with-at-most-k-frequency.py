class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        count = defaultdict(int)
        l = res = 0
        cnt = 0  # count of numbers with freq > k
        for r in range(len(nums)):
            count[nums[r]] += 1
            cnt += count[nums[r]] > k
            if cnt > 0:
                cnt -= count[nums[l]] > k
                count[nums[l]] -= 1
                l += 1
        return len(nums) - l