from typing import List
from collections import deque

class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        bank = set(bank)
        
        def getNeighbors(gene: str):
            neighbors = []
            geneOptions = {'A', 'C', 'G', 'T'}
            
            for i in range(len(gene)):
                for mutation in geneOptions.difference(gene[i]):
                    neighbor = gene[:i] + mutation + gene[i+1:]
                    if neighbor in bank:
                        neighbors.append(neighbor)
            
            return neighbors
        
        queue = deque([(startGene, 0)])
        seen = set([startGene])

        while queue:
            gene, steps = queue.popleft()

            if gene == endGene:
                return steps
            
            for neighbor in getNeighbors(gene):
                if neighbor not in seen:
                    seen.add(neighbor)
                    queue.append((neighbor, steps + 1))

        return -1

def main():
    runner = Solution()

    startGene = "AACCGGTT"
    endGene = "AACCGGTA"
    bank = ["AACCGGTA"]
    ans = runner.minMutation(startGene, endGene, bank)
    print(ans)

if __name__ == "__main__":
    main()