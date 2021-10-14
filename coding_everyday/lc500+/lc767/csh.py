import collections
class Solution(object):
    def reorganizeString(self, S):
        """
        :type S: str
        :rtype: str
        """
        counter = collections.Counter(S)
        max_time = counter.most_common(1)[0][1]
        if max_time > (len(S) + 1) / 2:
            return ""

        rst = ""
        common = [list(i) for i in counter.most_common()]
        insert_idx = 0
        pos = True
        while common:
            ch = ''
            if pos:
                ch = common[0][0]
                ch_pos = 0
            else:
                ch = common[-1][0]
                ch_pos = -1

            if len(rst) > 0 and rst[-1] == ch:
                rst = rst[:insert_idx] + ch + rst[insert_idx:]
                insert_idx += 2
            else:
                rst += ch

            common[ch_pos][1] -= 1
            if common[ch_pos][1] == 0:
                common.pop(ch_pos)
            pos = not pos
        return rst


if __name__ == "__main__":
    sol = Solution()
    S = 'ogccckcwmbmxtsbmozli'
    S = "nlmxhnpifuaxinxpxlcttjnlggmkjioewbecnofqpvcikiazmn"
    print sol.reorganizeString(S)
