class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        dist = [0 for people in range(num_people)]
        candies_left = candies
        for i in range(candies):
            if i >= candies_left:
                dist[i%num_people] += candies_left
                break
            else:
                dist[i%num_people] += i+1
                candies_left -= i+1
        return dist
