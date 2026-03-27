from typing import List


class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        n = len(img1)
        rst = 0
        for i in range(1, n*2):
            for j in range(1, n*2):
                # print('hhhhh', i-n, j-n)
                cnt = 0
                for k in range(max(n-i, 0), min(2*n-i, n)):
                    for l in range(max(n-j, 0), min(2*n-j, n)):
                        # print((k+i-n), (l+j-n), '--->', k, l)
                        if img1[k+i-n][l+j-n] == 1 and img2[k][l] == 1:
                            cnt += 1
                # print('----------', cnt)
                rst = max(rst, cnt)
        return rst


if __name__ == "__main__":
    sol = Solution()
    img1 = [[1, 1, 0], [0, 1, 0], [0, 1, 0]]
    img2 = [[0, 0, 0], [0, 1, 1], [0, 0, 1]]
    print(sol.largestOverlap(img1, img2))
