class Solution:
    def fib(self, n: int) -> int:
        #tabulation
        dp = collections.defaultdict(int)
        
        dp[1] = 1
        for i in range(2,n+1):
            dp[i]=dp[i-1]+dp[i-2]
        return dp[n]