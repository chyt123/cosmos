class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        if bound == 0:
            return []
        lx = ceil(log(bound, x)) if x > 1 else 1
        ly = ceil(log(bound, y)) if y > 1 else 1

        ans = set()
        for i in range(lx):
            for j in range(ly):
                cur = x ** i + y ** j
                if cur <= bound:
                    ans.add(cur)
                else:
                    break
        return list(ans)