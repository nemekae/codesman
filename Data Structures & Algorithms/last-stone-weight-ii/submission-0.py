class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        total = sum(stones)
        target = total // 2

        dp = [False] * (target + 1)
        dp[0] = True

        for stone in stones:
            for s in range(target, stone - 1, -1):
                if dp[s - stone]:
                    dp[s] = True
        
        for s in range(target, -1, -1):
            if dp[s]:
                return total - 2 * s
        return total