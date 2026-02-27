class Solution(object):
    def numDistinct(self, s, t):
        n, m = len(s), len(t)
        if m == 0:
            return 1
        if n < m:
            return 0

        dp = [0] * (m + 1)
        dp[0] = 1

        for ch in s:
            for j in range(m, 0, -1):
                if ch == t[j - 1]:
                    dp[j] += dp[j - 1]

        return dp[m]
