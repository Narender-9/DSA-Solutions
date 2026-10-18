class Solution:
    def numOfWays(self, nums: list[int]) -> int:
        MOD=10**9+7
        n=len(nums)
        comb=[[0]*n for _ in range(n)]
        for i in range(n):
            comb[i][0]=comb[i][i]=1
            for j in range(1,i):
                comb[i][j]=(comb[i-1][j-1]+comb[i-1][j])%MOD
        def solve(arr):
            if len(arr)<=2:
                return 1
            root=arr[0]
            l=[x for x in arr if x<root]
            r=[x for x in arr if x>root]
            wl=solve(l)
            wr=solve(r)
            w=comb[len(l)+len(r)][len(l)]
            return w*wl%MOD*wr%MOD
        return (solve(nums)-1)%MOD