from typing import List

class Solution:
    def maximizeEfficiencyProduct(self, efficiencyScores: List[int]) -> int:
        if len(efficiencyScores) < 5:
            return 0
        
        inc_scores = sorted(efficiencyScores) # [-8, -7, -1, 1, 2, 3, 4, 5]
        dec_scores = inc_scores[::-1] # [5, 4, 3, 2, 1, -1, -7, -8]
        n = len(inc_scores)
        prod = 1
        small_pointer = 0
        big_pointer = 0
        
        while small_pointer + big_pointer < 5:
            biggest, smallest = dec_scores[big_pointer], inc_scores[small_pointer]
            if small_pointer < n-1 and big_pointer < n-1:
                if smallest * inc_scores[small_pointer+1] > biggest * dec_scores[big_pointer+1]:
                    prod *= smallest * inc_scores[small_pointer+1]
                    small_pointer += 2
                    continue
            
            prod *= biggest
            big_pointer += 1
        
        return prod

if __name__ == "__main__":
    runner = Solution()
    voucher_input = 3
    input = [-8, -7, -1, 1, 2, 3, 4, 5]
    answer = 3360
    output = runner.maximizeEfficiencyProduct(input)
    print(f"{input} = {output}")
    assert(output == answer)