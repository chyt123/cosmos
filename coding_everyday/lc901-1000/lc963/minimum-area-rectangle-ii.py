class Solution:
    def minAreaFreeRect(self, points: List[List[int]]) -> float:
        n = len(points)
        s = set()
        for px, py in points:
            s.add((px, py))
        min_area = float('inf')
        for i, j, k in itertools.permutations(points, 3):
            xi, yi = i[0], i[1]
            xj, yj = j[0], j[1]
            xk, yk = k[0], k[1]

            dx = xi - xj
            dy = yi - yj
            xl = xk + dx
            yl = yk + dy
            if (xl, yl) in s:
                v1 = (xi - xj, yi - yj)
                v2 = (xi - xl, yi - yl)
                # x1*x2 + y1*y2 = 0
                dot_product = v1[0] * v2[0] + v1[1] * v2[1]
                if abs(dot_product) < 1e-7:
                    a = sqrt((xi - xj)**2 + (yi - yj)**2)
                    b = sqrt((xi - xl)**2 + (yi - yl)**2)
                    # print((xi, yi), (xj, yj), (xk, yk), (xl, yl))
                    # print(a, b)
                    min_area = min(min_area, a * b)
        return min_area if min_area < float('inf') else 0