class Solution:
    def maxSum(self, nums: List[int], k: int) -> int:
        MOD=10**9+7
        bitcount=[0]*32
        for x in nums:
            for i in range(32):
                if (x>>i)&1:
                    bitcount[i]+=1
        new=[0]*k
        for i in range(k):
            cur=0
            for bit in range(31,-1,-1):
                if bitcount[bit]>0:
                    cur|=1 << bit
                    bitcount[bit]-=1
            new[i]=cur
        ans=0
        for x in new:
            ans=(ans+x*x)%MOD
        return ans