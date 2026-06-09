class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:
        normal_li = [label]

        while label > 1:
            label //= 2
            normal_li.append(label)
        normal_li.reverse()
        n = len(normal_li)
        for i in range(n):
            if i % 2 == n % 2:
                su = 3 * 2 ** i - 1
                normal_li[i] = su - normal_li[i]
        return normal_li
#   1
#  2 3
# 45 67
