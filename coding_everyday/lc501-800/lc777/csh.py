class Solution(object):
    def canTransform(self, start, end):
        """
        :type start: str
        :type end: str
        :rtype: bool
        """
        if len(start) != len(end):
            return False

        bone_start = start.replace("X", "")
        bone_end = end.replace("X", "")
        if bone_start != bone_end:
            return False

        r_cnt = l_cnt = 0
        for i in range(len(start)):
            if start[i] == 'R':
                r_cnt += 1
            if end[i] == 'R':
                r_cnt -= 1

            if start[i] == 'L':
                l_cnt += 1
            if end[i] == 'L':
                l_cnt -= 1

            if r_cnt < 0 or l_cnt > 0:
                return False

        return True


if __name__ == "__main__":
    sol = Solution()
    start = "RXXLRXRXL"
    end = "XRLXXRRLX"
    print sol.canTransform(start, end)
