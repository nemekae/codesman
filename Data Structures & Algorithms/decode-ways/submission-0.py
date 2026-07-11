class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == '0':
            return 0
        
        n = len(s)
        # prev2 = ways to decode s[:i-2], prev1 = ways to decode s[:i-1]
        prev2, prev1 = 1, 1  # dp[0] = 1 (empty string), dp[1] = 1 (first char valid)
        
        for i in range(1, n):
            current = 0
            
            one_digit = int(s[i])
            two_digit = int(s[i - 1:i + 1])
            
            if one_digit >= 1:               # single digit 1-9 is valid
                current += prev1
            if 10 <= two_digit <= 26:         # two digits 10-26 is valid
                current += prev2
            
            prev2, prev1 = prev1, current
        
        return prev1