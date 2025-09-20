from typing import List

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for asteroid in asteroids:
            while stack and stack[-1] > 0 and asteroid < 0:
                if abs(stack[-1]) < abs(asteroid):
                    stack.pop()
                elif abs(stack[-1]) > abs(asteroid):
                    break
                else:
                    stack.pop()
                    break
            else:
                stack.append(asteroid)

        return stack
    
if __name__ == "__main__":
    runner = Solution()
    asteroids = [-2,2,1,-2]
    ans = runner.asteroidCollision(asteroids)
    print(ans)
    print("exp ans:", [-2])