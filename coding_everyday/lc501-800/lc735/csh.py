class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        ptr = 0
        while ptr < len(asteroids) - 1:
            print asteroids, ptr
            # collision
            if asteroids[ptr] > 0 > asteroids[ptr + 1]:
                if -asteroids[ptr + 1] > asteroids[ptr]:
                    asteroids.pop(ptr)
                    ptr = ptr - 1 if ptr > 0 else ptr
                    continue
                elif -asteroids[ptr + 1] < asteroids[ptr]:
                    asteroids.pop(ptr + 1)
                    continue
                elif -asteroids[ptr + 1] == asteroids[ptr]:
                    asteroids.pop(ptr)
                    asteroids.pop(ptr)
                    ptr = ptr - 1 if ptr > 0 else ptr
                    continue
            ptr += 1
        return asteroids


if __name__ == "__main__":
    sol = Solution()
    asteroids = [8, -8]
    print sol.asteroidCollision(asteroids)
