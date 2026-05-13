class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        ans = firstList.copy()

        i1 = 0
        i2 = 0
        while i1 < len(ans) and i2 < len(secondList):
            # print(ans[i1], secondList[i2])
            start1, end1 = ans[i1]
            start2, end2 = secondList[i2]

            if start2 > end1:
                ans[i1: i1 + 1] = []
                continue
            if end2 < start1:
                i2 += 1
                continue

            if start2 >= start1:
                if end2 >= end1:
                    ans[i1] = [start2, end1]
                else:
                    ans[i1: i1 + 1] = [[start2, end2], [end2 + 1, end1]]
            else:
                if end2 < end1:
                    ans[i1: i1 + 1] = [[start1, end2], [end2 + 1, end1]]
                    i2 += 1
            i1 += 1
            # print(ans, secondList)

        if i1 < len(ans):
            ans[i1:] = []
        return ans
