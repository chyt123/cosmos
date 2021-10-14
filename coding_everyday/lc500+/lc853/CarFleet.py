from typing import List
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = {}
        for idx, i in enumerate(position):
            cars[i] = speed[idx]
        s_cars = sorted(cars.items(), reverse=True)
        fleet = []
        for idx, (car, speed) in enumerate(s_cars):
            cur_t = (target - car) / speed
            if idx == 0 or cur_t > fleet[-1]:  # first car or cannot join and start a new fleet
                fleet.append(cur_t)
        return len(fleet)


if __name__ == "__main__":
    sol = Solution()
    target = 12
    position = [10, 8, 0, 5, 3]
    speed = [2, 4, 1, 1, 3]
    print(sol.carFleet(target, position, speed))
