from collections import Counter
class Solution(object):
    def numRabbits(self, answers):
        """
        :type answers: List[int]
        :rtype: int
        """
        if not answers:
            return 0
        answers = sorted(answers)
        pre = -1
        cnt = 0
        while answers:
            now = answers.pop(0)
            if now != pre:
                cnt += now + 1
                total = now
                pre = now
            else:
                if total == 0:
                    cnt += now + 1
                    total = now
                else:
                    total -= 1

        return cnt

    # def numRabbits(self, answers):
    #     if not answers: return 0
    #     res = 0
    #     for a, b in collections.Counter(answers).items():
    #         div = b // (a + 1)
    #         mod = b % (a + 1)
    #         res += (a + 1) * div
    #         if mod != 0: res += (a + 1)
    #     return res

if __name__ == "__main__":
    sol = Solution()
    answers = [1,0,1,0,0]
    print sol.numRabbits(answers)

