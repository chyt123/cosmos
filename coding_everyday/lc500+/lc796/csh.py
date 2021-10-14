class Solution(object):
    def rotateString(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        if B == "":
            return A == ""
        idx = 0
        while idx != -1:
            idx = A.find(B[0], idx)
            print idx
            new_A = A[idx:] + A[0:idx]
            if idx == -1:
                break
            else:
                idx += 1
            if new_A == B:
                return True
        return False


if __name__ == "__main__":
    sol = Solution()
    A = "1111"
    B = "fufrwpiddgyynfujnqblngzoogzgvcuszhlbtpmksjleuchmjf"
    print sol.rotateString(A, B)

