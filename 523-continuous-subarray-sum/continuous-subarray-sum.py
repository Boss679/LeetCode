class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        hashmap = {}
        hashmap[0]=-1
        summ=0
        for i,j in enumerate(nums):
            summ+=j
            if summ%k in hashmap.keys():
                if i-hashmap[summ%k]>=2:
                    return True
                else:
                    continue
            hashmap[summ%k]=i
        return False