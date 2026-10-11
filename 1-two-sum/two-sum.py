class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d={}
        for i,num in enumerate(nums):
            req=target-num
            if req in d:
                return [d[req],i]
            d[num]=i