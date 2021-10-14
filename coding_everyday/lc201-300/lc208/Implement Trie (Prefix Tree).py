import collections
import math
from typing import List
from collections import defaultdict
from util import lc_list2tree, TreeNode, lc_tree2list


class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.d = {}

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        cur = self.d
        for i in word:
            if i not in cur:
                cur[i] = {}
            cur = cur[i]
        cur["isval"] = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        cur = self.d
        for i in word:
            if i not in cur:
                return False
            cur = cur[i]
        return "isval" in cur

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        cur = self.d
        for i in prefix:
            if i not in cur:
                return False
            cur = cur[i]
        return True


if __name__ == "__main__":
    trie = Trie()
    cmds = ["Trie", "insert", "search", "search", "startsWith", "insert", "search", ]
    args = [[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
    for idx, i in enumerate(cmds):
        if i == 'insert':
            trie.insert(args[idx][0])
        elif i == 'search':
            print(trie.search(args[idx][0]))
        elif i == 'startsWith':
            print(trie.startsWith(args[idx][0]))
