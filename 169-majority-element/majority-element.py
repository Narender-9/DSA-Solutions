class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ct=0
        stu=0
        for num in nums:
            if ct==0:
                stu=num
            if num==stu:
                ct+=1
            else:
                ct-=1
        return stu