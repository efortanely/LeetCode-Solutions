class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counter = Counter(arr)
        occurences = set(counter.values())

        return len(occurences) == len(counter.values())