from collections import deque

class StockSpanner:
    def __init__(self):        
        self.day = 0
        self.decreasing = deque()

    def next(self, price: int) -> int:
        self.day += 1
        
        popped = False
        while self.decreasing and price >= self.decreasing[-1][0]:
            popped = True
            self.decreasing.pop()
        
        if not popped:
            ans = 1
        else:
            first_day = 0 if not self.decreasing else self.decreasing[-1][1]
            ans = self.day - first_day

        self.decreasing.append((price, self.day))

        return ans

def main():
    stock_spanner = StockSpanner()

    print(stock_spanner.next(28))
    print(stock_spanner.next(14))
    print(stock_spanner.next(28))

# [ (100, day 1) ] added - 1
# [ (100, day 1), (80, day 2) ] added - 1
# [ (100, day 1), (80, day 2), (60, day 3) ] added - 1
# [ (100, day 1), (80, day 2), (70, day 4) ] deleted, day 4 - day 2
# [ (100, day 1), (80, day 2), (70, day 4), (60, day 5) ] added - 1
# [ (100, day 1), (80, day 2), (75, day 6) ] deleted, day 6 - day 2
# [ (100, day 1), (85, day 7) ] deleted, day 7 - day 1

# [ (31, day 1) ] added - 1
# [ (41, day 2) ] deleted, day 2 - day 1

if __name__ == "__main__":
    main()