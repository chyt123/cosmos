from collections import defaultdict
class WordFilter(object):

    def __init__(self, words):
        """
        :type words: List[str]
        """
        self.prefixes = defaultdict(set)
        self.suffixes = defaultdict(set)
        self.weight = dict()
        for idx, word in enumerate(words):
            for i in range(len(word) + 1):
                self.prefixes[word[:i]].add(word)
            for i in range(len(word), -1, -1):
                self.suffixes[word[i:]].add(word)
            self.weight[word] = idx
        print self.prefixes
        print self.suffixes

    def f(self, prefix, suffix):
        """
        :type prefix: str
        :type suffix: str
        :rtype: int
        """
        max_weight = -1
        for item in self.prefixes[prefix] & self.suffixes[suffix]:
            if self.weight[item] > max_weight:
                max_weight = self.weight[item]
        return max_weight


# Your WordFilter object will be instantiated and called as such:
if __name__ == "__main__":
    # words = ["apple", "aasdfe"]
    # [prefix, suffix] = ["a","e"]
    words = ["pop"]
    [prefix, suffix] = ["",""]
    obj = WordFilter(words)
    print obj.f(prefix,suffix)
