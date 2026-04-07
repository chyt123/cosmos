class Solution:
    def prisonAfterNDays(self, cells: List[int], n: int) -> List[int]:
        cur = [0] * 8
        pre = cells.copy()

        n = (n - 1) % 14 + 1
        for i in range(n):
            for j in range(8):
                if j == 0 or j == 7:
                    cur[j] = 0
                elif pre[j - 1] == pre[j + 1]:
                    cur[j] = 1
                else:
                    cur[j] = 0
            pre = cur.copy()

        return cur

                