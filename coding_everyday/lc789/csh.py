class Solution(object):
    def escapeGhosts(self, ghosts, target):
        """
        :type ghosts: List[List[int]]
        :type target: List[int]
        :rtype: bool
        """
        pac_dist = self.cal_dist(target)
        for ghost in ghosts:
            gho_dist = self.cal_dist(ghost, target)
            if gho_dist <= pac_dist:
                return False

        return True

    def cal_dist(self, cord1, cord2=[0, 0]):
        return abs(cord1[0] - cord2[0]) + abs(cord1[1] - cord2[1])


if __name__ == "__main__":
    sol = Solution()
    ghosts = [[2, 0]]
    target = [1, 0]
    print sol.escapeGhosts(ghosts, target)

