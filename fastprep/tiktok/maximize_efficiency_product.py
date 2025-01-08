from typing import List

class Solution:
    def maximizeEfficiencyProduct(self, efficiencyScores: List[int]) -> int:
        if len(efficiencyScores) < 5:
            return 0
        
        efficiencyScores.sort()
        n = len(efficiencyScores)
        prod = 1
        small_pt = 0
        big_pt = n-1
        count = 0
        
        while count < 5:
            if small_pt + 1 < big_pt:
                smallest_pair_prod = efficiencyScores[small_pt] * efficiencyScores[small_pt+1]
                largest_single = efficiencyScores[big_pt]

                if smallest_pair_prod > largest_single:
                    prod *= smallest_pair_prod
                    small_pt += 2
                    count += 2
                    continue
                else:
                    prod *= largest_single
                    big_pt -= 1
                    count += 1
                    continue
            else:
                prod *= efficiencyScores[big_pt]
                big_pt -= 1
                count += 1
                continue
        
        return prod

if __name__ == "__main__":
    runner = Solution()
    voucher_input = 3
    input = [-8, -7, -1, 1, 2, 3, 4, 5]
    answer = 3360
    output = runner.maximizeEfficiencyProduct(input)
    print(f"{input} = {output}")
    assert(output == answer)

