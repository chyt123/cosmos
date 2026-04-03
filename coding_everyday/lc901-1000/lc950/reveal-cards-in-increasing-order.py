class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        n = len(deck)
        deck = sorted(deck)
        idx = deque([i for i in range(n)])
        order = []
        ans = [0] * n
        flag = True

        while idx:
            if flag:
                order.append(idx.popleft())
            else:
                idx.append(idx.popleft())
            flag = not flag

        # print(order)
        for i, o in enumerate(order):
            ans[o] = deck[i]

        return ans

# 2 3 5 7 11 13 17
# 0  1  2  3  4  5  6
# 0  2  4  6  3  1  5
# 2  3  5  7  11 13 17
# 2 13 3 11 5