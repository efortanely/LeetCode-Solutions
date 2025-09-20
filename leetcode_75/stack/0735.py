from typing import List

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for asteroid in asteroids:
            if stack:
                last_asteroid = stack[-1]

                if last_asteroid > 0 and asteroid < 0:
                    if abs(last_asteroid) < abs(asteroid):
                        stack.pop()
                        last_asteroid = stack[-1]
                        append_asteroid = True

                        while last_asteroid > 0 and asteroid < 0:
                            if abs(last_asteroid) < abs(asteroid):
                                stack.pop()
                            elif abs(asteroid) < abs(last_asteroid):
                                append_asteroid = False
                                break
                            else:
                                stack.pop()

                            last_asteroid = stack[-1]
                        
                        if append_asteroid:
                            stack.append(asteroid)
                    elif abs(asteroid) < abs(last_asteroid):
                        pass
                    else:
                        stack.pop()
                else:
                    stack.append(asteroid)
            else:
                stack.append(asteroid)

        return stack
    
if __name__ == "__main__":
    runner = Solution()
    asteroids = [10,2,-5]
    ans = runner.asteroidCollision(asteroids)
    print(ans)
    print("exp ans:", [10])