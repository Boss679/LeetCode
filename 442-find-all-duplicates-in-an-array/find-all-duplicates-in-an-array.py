class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        count = Counter(nums)
        res = []

        for num in count:
            if count[num] == 2:
                res.append(num)
        
        return res