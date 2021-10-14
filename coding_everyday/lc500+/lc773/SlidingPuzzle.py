from typing import List


class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        def slide_up(state, pos_zero):
            l = list(state)
            l[pos_zero], l[pos_zero - 3] = l[pos_zero - 3], l[pos_zero]
            return ''.join(l)

        def slide_down(state, pos_zero):
            l = list(state)
            l[pos_zero], l[pos_zero + 3] = l[pos_zero + 3], l[pos_zero]
            return ''.join(l)

        def slide_left(state, pos_zero):
            l = list(state)
            l[pos_zero], l[pos_zero - 1] = l[pos_zero - 1], l[pos_zero]
            return ''.join(l)

        def slide_right(state, pos_zero):
            l = list(state)
            l[pos_zero], l[pos_zero + 1] = l[pos_zero + 1], l[pos_zero]
            return ''.join(l)

        def find_doable(pos_zero):
            rst = []
            if pos_zero <= 2:  # upside
                rst.append(slide_down)
            else:  # downside
                rst.append(slide_up)

            if pos_zero in [0, 3]:  # can't go left
                rst.append(slide_right)
            elif pos_zero in [2, 5]:  # can't go right
                rst.append(slide_left)
            else:
                rst.append(slide_left)
                rst.append(slide_right)
            return rst

        visit = []
        queue = [-1]
        state = ''.join(str(i) for inner in board for i in inner)
        if state == '123450':
            return 0
        queue.append(state)
        level = -1
        while not state == '123450':
            state = queue.pop(0)
            if isinstance(state, int):  # level indicator
                if not queue:
                    return -1
                level += 1
                queue.append(level)
                continue
            visit.append(state)
            pos_zero = state.find('0')
            for func in find_doable(pos_zero):
                new_state = func(state, pos_zero)
                if new_state not in visit:
                    queue.append(new_state)
        return level


if __name__ == "__main__":
    sol = Solution()
    board = [[4, 1, 2], [5, 0, 3]]
    board = [[1, 2, 3], [4, 0, 5]]
    board = [[3, 2, 4], [1, 5, 0]]
    board = [[1, 2, 3], [5, 4, 0]]
    print(sol.slidingPuzzle(board))
