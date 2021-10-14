from typing import List
class Solution:
    def ambiguousCoordinates(self, S: str) -> List[str]:
        ret = set()
        raw_num = S[1:-1]
        for i in range(1, len(raw_num)):
            left_num = raw_num[:i]
            right_num = raw_num[i:]
            for j in range(0, len(left_num)):
                for k in range(0, len(right_num)):
                    new_left = left_num[:j] + '.' + left_num[j:]
                    new_right = right_num[:k] + '.' + right_num[k:]
                    if new_left.startswith('.'):
                        new_left = new_left[1:]
                    if new_right.startswith('.'):
                        new_right = new_right[1:]
                    if self.check_string(new_left) and self.check_string(new_right):
                        ret.add('({}, {})'.format(new_left, new_right))
        return list(ret)

    @staticmethod
    def check_string(s: str):
        if s == '0':
            return True
        if s.startswith('0') and not s.startswith('0.'):
            return False
        if '.' in s and s.endswith('0'):
            return False
        return True


if __name__ == "__main__":
    sol = Solution()
    S = "(123)"
    print(sol.ambiguousCoordinates(S))
