from collections import deque

class MovingAverage:
    def __init__(self, size: int):
        self.window = size
        self.queue = deque()
        self.cur_sum = 0


    def next(self, val: int) -> float:
        self.queue.append(val)
        self.cur_sum += val

        while len(self.queue) > self.window:
            remove = self.queue.popleft()
            self.cur_sum -= remove
        
        return self.cur_sum / len(self.queue)

def main():
    moving_average = MovingAverage(3)
    
    print(moving_average.next(1))
    print(moving_average.next(10))
    print(moving_average.next(3))
    print(moving_average.next(5))

if __name__ == "__main__":
    main()