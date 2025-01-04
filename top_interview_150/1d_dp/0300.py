from typing import List

class SegmentTree:
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (4 * n)

    def build(self, node, start, end):
        if start == end:
            self.tree[node] = 0
        else:
            mid = (start + end) // 2
            left_child = 2 * node + 1
            right_child = 2 * node + 2
            self.build(left_child, start, mid)
            self.build(right_child, mid + 1, end)
            self.tree[node] = max(self.tree[left_child], self.tree[right_child])

    def query(self, node, start, end, l, r):
        if r < start or l > end:
            return 0

        if l <= start and end <= r:
            return self.tree[node]

        mid = (start + end) // 2
        left_child = 2 * node + 1
        right_child = 2 * node + 2
        left_query = self.query(left_child, start, mid, l, r)
        right_query = self.query(right_child, mid + 1, end, l, r)
        return max(left_query, right_query)

    def update(self, node, start, end, idx, value):
        if start == end:
            self.tree[node] = value
        else:
            mid = (start + end) // 2
            left_child = 2 * node + 1
            right_child = 2 * node + 2
            if start <= idx <= mid:
                self.update(left_child, start, mid, idx, value)
            else:
                self.update(right_child, mid + 1, end, idx, value)
            self.tree[node] = max(self.tree[left_child], self.tree[right_child])

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        sorted_nums = sorted(set(nums))
        n = len(sorted_nums)
        seg_tree = SegmentTree(len(sorted_nums))
        num_to_idx = {num: idx for idx, num in enumerate(sorted_nums)}
        max_length = 0

        for num in nums:
            curr_idx = num_to_idx[num]

            if curr_idx > 0:
                max_prev_length = seg_tree.query(0, 0, n-1, 0, curr_idx-1)
            else:
                max_prev_length = 0

            length = max_prev_length + 1
            seg_tree.update(0, 0, n-1, curr_idx, length)
            max_length = max(max_length, length)

        return max_length if max_length else 1
    
if __name__ == "__main__":
    runner = Solution()
    nums = [10,9,2,5,3,7,101,18]
    ans = runner.lengthOfLIS(nums)
    print(ans)