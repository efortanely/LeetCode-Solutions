from typing import List
from collections import defaultdict, deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in set(wordList):
            return 0
        
        word_list = wordList
        word_list.append(beginWord)

        graph = defaultdict(list)

        for i in range(len(word_list)):
            word_1 = word_list[i]

            for j in range(i+1, len(word_list)):
                word_2 = word_list[j]

                diff_chars = 0

                for k in range(len(word_1)):
                    if word_1[k] != word_2[k]:
                        diff_chars += 1

                    if diff_chars > 1:
                        break

                if diff_chars == 1:
                    graph[word_1].append(word_2)
                    graph[word_2].append(word_1)

        seen = {beginWord}
        queue = deque([(beginWord, 1)])

        while queue:
            word, steps = queue.popleft()

            if word == endWord:
                return steps
            
            for neighbor in graph[word]:
                if neighbor not in seen:
                    seen.add(neighbor)
                    queue.append((neighbor, steps + 1))

        return 0

def main():
    runner = Solution()

    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot","dot","dog","lot","log","cog"]

    ans = runner.ladderLength(beginWord, endWord, wordList)
    print(ans)

if __name__ == "__main__":
    main()