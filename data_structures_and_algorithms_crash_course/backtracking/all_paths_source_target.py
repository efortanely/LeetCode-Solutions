from typing import List

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        def backtrack(curr, num):
            if num == len(graph) - 1:
                ans.append(curr[:])

            for child in graph[num]:
                curr.append(child)
                backtrack(curr, child)
                curr.pop()

        ans = []
        backtrack([0], 0)
        return ans

def main():
    runner = Solution()
    graph = [[1,2],[3],[3],[]]
    ans = runner.allPathsSourceTarget(graph)
    print(ans)

if __name__ == "__main__":
    main()