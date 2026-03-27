from collections import deque

class Solution(object):
    def next_num(self, ch):
        if ch == '9':
            return str(0)
        return str(int(ch) + 1)

    def prev_num(self, ch):
        if ch == '0':
            return str(9)
        return str(int(ch) - 1)

    def openLock(self, deadends, target):
        if '0000' in deadends:
            return -1
        visited = set(deadends)
        dq = deque()
        dq.append('0000')
        cnt = -1

        while dq:
            size = len(dq)
            cnt += 1
            for _ in range(size):
                cur = dq.popleft()
                if cur == target:
                    return cnt

                for idx, ch in enumerate(cur):
                    list_cur = list(cur)
                    list_cur[idx] = self.next_num(ch)
                    tmp = ''.join(list_cur)

                    if tmp not in visited:
                        dq.append(tmp)
                        visited.add(tmp)

                    list_cur[idx] = self.prev_num(ch)
                    tmp = ''.join(list_cur)

                    if tmp not in visited:
                        dq.append(tmp)
                        visited.add(tmp)
        return -1


if __name__ == "__main__":
    sol = Solution()
    deadends = ["0201", "0101", "0102", "1212", "2002"]
    target = "0202"
    deadends = ["8888"]
    target = "0009"
    deadends = ["8887", "8889", "8878", "8898", "8788", "8988", "7888", "9888"]
    target = "8888"
    deadends = ["0000"]
    target = "8888"
    print sol.openLock(deadends, target)
