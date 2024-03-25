class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashet = set()

        for n in nums:
            if n in hashet:
                return True
            hashet.add(n)
        return False
