# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def print_list(self, listnode):
        node = listnode
        while node:
            print node.val,
            node = node.next
        print

    def splitListToParts(self, root, k):
        """
        :type root: ListNode
        :type k: int
        :rtype: List[ListNode]
        """
        node = root
        cnt = 0
        while node:
            cnt += 1
            node = node.next
        remainder = cnt % k
        quo = cnt / k
        ans = list()

        print quo, remainder
        node = root
        for i in range(k):
            tmp = list()
            if i < remainder:
                for j in range(quo + 1):
                    if node:
                        tmp.append(node.val)
                        node = node.next
                ans.append(tmp)
            else:
                for j in range(quo):
                    if node:
                        tmp.append(node.val)
                        node = node.next
                ans.append(tmp)

        print ans
        ret = list()
        for i in ans:
            head = None
            for idx, ele in enumerate(i):
                if idx == 0:
                    tmp = ListNode(ele)
                    head = tmp
                else:
                    tmp.next = ListNode(ele)
                    tmp = tmp.next
            ret.append(head)

        for i in ret:
            self.print_list(i)
        return ret


if __name__ == "__main__":
    root = ListNode(1)
    two = ListNode(2)
    three = ListNode(3)
    four = ListNode(4)
    five = ListNode(5)
    root.next = two
    two.next = three
    three.next = five
    five.next = four
    k = 6
    sol = Solution()
    print sol.splitListToParts(root, k)
