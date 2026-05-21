class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        n = len(tops)
        swap_top, swap_bottom = 0, 0
        target_top = tops[0]
        target_bottom = bottoms[0]
        flag_top, flag_bottom = True, True
        same_cnt = 0 if target_top != target_bottom else 1
        for i in range(1, n):
            if tops[i] == bottoms[i]:
                same_cnt += 1

            if flag_top and tops[i] != target_top:
                if bottoms[i] != target_top:
                    flag_top = False
                else:
                    swap_top += 1

            if flag_bottom and bottoms[i] != target_bottom:
                if tops[i] != target_bottom:
                    flag_bottom = False
                else:
                    swap_bottom += 1

            if not flag_top and not flag_bottom:
                return -1

        # print(n, flag_top, flag_bottom, swap_top, swap_bottom)
        swap_top = min(swap_top, n - swap_top - same_cnt)
        swap_bottom = min(swap_bottom, n - swap_bottom - same_cnt)

        if flag_top and flag_bottom:
            return min(swap_top, swap_bottom)
        if flag_top:
            return swap_top
        return swap_bottom


# test cases
# n = 1 => 0

