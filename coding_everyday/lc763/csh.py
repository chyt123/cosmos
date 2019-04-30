class Solution(object):
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        dic = dict()
        for idx, ch in enumerate(S):
            if ch not in dic.keys():
                dic[ch] = [idx, idx]
            else:
                dic[ch][1] = idx

        dic = dic.values()
        dic.sort(key=lambda x: x[0])
        ran = dic[0]
        rst = []
        for item in dic:
            if ran[0] < item[0] < ran[1] < item[1]:  # expand range
                ran[1] = item[1]
                continue
            if item[0] > ran[1]:  # new range:
                rst.append(ran)
                ran = item

        rst.append(ran)
        for idx, i in enumerate(rst):
            rst[idx] = i[1] - i[0] + 1
        return rst


if __name__ == "__main__":
    sol = Solution()
    S = 'ababcbacadefegdehijhklij'
    print sol.partitionLabels(S)
