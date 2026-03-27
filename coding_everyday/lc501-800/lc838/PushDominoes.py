import re
class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        # visit = [False for _ in dominoes]
        # for i in re.finditer('R\.*L', dominoes):
        #     start, end = i.span()
        #     for j in range(start, end):
        #         if j < (start+end-1)/2:
        #             dominoes = dominoes[:j] + 'R' + dominoes[j+1:]
        #         elif j > (start+end-1)/2:
        #             dominoes = dominoes[:j] + 'L' + dominoes[j+1:]
        #         visit[j] = True

        # for i in range(1, len(dominoes)):
        #     if not visit[i] and dominoes[i] == '.' and dominoes[i-1] == 'R':
        #         dominoes = dominoes[:i] + 'R' + dominoes[i+1:]

        # for i in range(len(dominoes)-2, -1, -1):
        #     if not visit[i] and dominoes[i] == '.' and dominoes[i+1] == 'L':
        #         dominoes = dominoes[:i] + 'L' + dominoes[i+1:]

        # return dominoes
        dominoes = 'L' + dominoes + 'R'
        for i in re.finditer('\.+', dominoes):
            start, end = i.span()
            if start == 0 and end == len(dominoes):
                return dominoes
            if start-1 < 0 or end >= len(dominoes) or dominoes[start-1] == dominoes[end]:
                ch = dominoes[start-1] if start-1 >= 0 else dominoes[end]
                dominoes = dominoes[:start] + ch * (end - start) + dominoes[end:]
            elif dominoes[start-1] == 'R' and dominoes[end] == 'L':
                num = (end-start) / 2
                if int(num) == num:
                    num = int(num)
                    ch = 'R' * num + 'L' * num
                else:
                    num = int(num)
                    ch = 'R' * num + '.' + 'L' * num
                dominoes = dominoes[:start] + ch + dominoes[end:]
        return dominoes[1:-1]


if __name__ == "__main__":
    sol = Solution()
    dominoes = ".L.R...LR..L.."
    dominoes = "RL.LR...L..R..LLR."
    dominoes = ".L.R...LR..L.."
    print(sol.pushDominoes(dominoes))
