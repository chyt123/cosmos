from typing import List
class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        size = len(image[0])
        for row in image:
            for i in range((size+1)//2):
                tmp = row[i]
                row[i] = - row[size-i-1] + 1
                row[size-i-1] = - tmp + 1
        return image


if __name__ == "__main__":
    sol = Solution()
    image = [[1, 1, 0, 0, 1], [1, 0, 0, 1, 1], [1, 0, 1, 1, 1], [0, 1, 0, 1, 0]]
    image = [[1, 1, 0, 0], [1, 0, 0, 1], [0, 1, 1, 1], [1, 0, 1, 0]]
    image = [[1, 1, 0], [1, 0, 1], [0, 0, 0]]
    print(sol.flipAndInvertImage(image))
