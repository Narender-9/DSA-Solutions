class Solution:
    def uniquePaths(self, grid: List[List[int]]) -> int:
        MOD=10**9 + 7
        n=len(grid[0])
        dp=[0]*n
        dp[0]=1
        for i in range(len(grid)):
            left=0
            for j in range(n):
                if grid[i][j]==1:
                    left,dp[j]=dp[j],left
                else:
                    left=(left+dp[j]) % MOD
                    dp[j]=left
        return dp[n-1]