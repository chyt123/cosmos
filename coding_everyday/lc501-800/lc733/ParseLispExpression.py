from typing import List


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        lx = len(image)
        ly = len(image[0])
        visit = [[False for _ in i] for i in image]

        def dps(image, x, y, start_color, newColor):
            if 0 <= x < lx and 0 <= y < ly and not visit[x][y] and image[x][y] == start_color:
                visit[x][y] = True
                image[x][y] = newColor
                dps(image, x - 1, y, start_color, newColor)
                dps(image, x + 1, y, start_color, newColor)
                dps(image, x, y - 1, start_color, newColor)
                dps(image, x, y + 1, start_color, newColor)

        start_color = image[sr][sc]
        dps(image, sr, sc, start_color, newColor)
        return image


if __name__ == "__main__":
    sol = Solution()
    # image = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
    # sr = 1
    # sc = 1
    # newColor = 2
    image = [[1, 1, 2, 1], [1, 1, 1, 2], [0, 0, 1, 0], [1, 0, 1, 0]]
    sr = 1
    sc = 0
    newColor = 2
    # image = [[0, 0, 0], [0, 1, 1]]
    # sr = 1
    # sc = 1
    # newColor = 1
    print(sol.floodFill(image, sr, sc, newColor))