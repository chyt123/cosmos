class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        v = set()
        ans = 0


        for i in stones:
            if (i[0], i[1]) not in v:
                v.add((i[0], i[1]))
                stack = [i]
                cnt = -1
                while len(stack):
                    l = stack.pop()
                    cnt += 1
                    for j in stones:
                        if (j[0], j[1]) not in v and (j[0] == l[0] or j[1] == l[1]):
                            stack.append(j)
                            v.add((j[0], j[1]))

                ans += cnt
        return ans


