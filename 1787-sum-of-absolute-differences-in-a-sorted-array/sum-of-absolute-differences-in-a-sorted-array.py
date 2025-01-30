class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n
        
        total_sum = sum(nums)
        prefix_sum = 0

        for i, num in enumerate(nums):
            total_sum -= nums[i]
            left_sum = i * nums[i] - prefix_sum
            right_sum = total_sum - (n - i - 1) * nums[i]
            res[i] = left_sum + right_sum
            prefix_sum += nums[i]
        
        return res