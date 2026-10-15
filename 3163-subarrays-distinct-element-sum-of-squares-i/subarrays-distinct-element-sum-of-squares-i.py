class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        totsum=0
        n=len(nums)
        for i in range(n):
            dele=set()
            for j in range(i,n):
                dele.add(nums[j])
                totsum+=len(dele)**2
        return totsum