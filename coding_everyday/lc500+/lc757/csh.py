class Solution(object):
    def intersectionSizeTwo(self, intervals):
        intervals.sort(key=lambda x: x[1])
        rst = list()
        print intervals
        for s, e in intervals:
            if len(rst) == 0 or rst[-1] < s:
                rst.append(e - 1)
                rst.append(e)
            elif rst[-2] < s:
                rst.append(e)

        print rst
        return len(rst)


if __name__ == "__main__":
    sol = Solution()
    intervals = [[2,10],[3,7],[3,15],[4,11],[6,12],[6,16],[7,8],[7,11],[7,15],[11,12]]
    # intervals = [[1,3],[1,4],[2,5],[3,5]]
    # intervals = [[1, 2], [2, 3], [2, 4], [4, 5]]
    # intervals = [[1,15],[0,8],[13,14]]
    # intervals = [[7,8],[0,14],[3,11]]
    # intervals = [[3,13],[2,8],[5,10]]
    print sol.intersectionSizeTwo(intervals)
