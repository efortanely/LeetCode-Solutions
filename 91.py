class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [-1 for i in range(len(s))]
        return self.numDecodingsHelper(s, 0, dp);

    def numDecodingsHelper(self, s: str, decodePointer: int, dp: List[int]) -> int:        
        if decodePointer == len(s):
            return 1
        elif decodePointer > len(s):
            return 0
        elif int(s[decodePointer]) == 0:
            return 0
        
        if dp[decodePointer] > -1:
            return dp[decodePointer]
    
        decodings = 0
        for i in range(1, 3):
            if decodePointer + i <= len(s):
                substr = s[decodePointer:decodePointer+i]
                if substr[0] != 0 and 1 <= int(substr) <= 26:
                    decodings += self.numDecodingsHelper(s, decodePointer+i, dp)
        
        dp[decodePointer] = decodings
        
        return dp[decodePointer]
