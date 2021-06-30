#coding=utf-8
import bisect
import collections
import sys


def minimalHeaviestSetA(arr):
    arr.sort()
    a = []
    sum_a = 0
    sum_b = sum(arr)
    while sum_a <= sum_b:
        cur = arr.pop()
        a.append(cur)
        sum_a += cur
        sum_b -= cur
    return a[::-1]

"""
    int[] mem = new int[s.length()];
    int count = 0;
    for (int i = 0; i < s.length(); ++i) {
        if (s.charAt(i) == '|') {
            mem[i] = count;
        } else {
            ++count;
        }
    }
    List<Integer> ans = new ArrayList<>();
    for (int i = 0; i < startIndices.size(); ++i) {
        int start = startIndices.get(i) - 1;
        int end = endIndices.get(i) - 1;
        
        while (start < end && s.charAt(start) != '|') ++start;
        while (start < end && s.charAt(end) != '|') --end;

        ans.add(mem[end] - mem[start]);
    }
    return ans;
}"""

def numberOfItems(s, startIndices, endIndices):
    mem = [0 for _ in range(len(s))]
    count = 0
    for i in range(len(s)):
        if s[i] == '|':
            mem[i] = count
        else:
            count += 1
    print(mem)
    ans = []
    for i in range(len(startIndices)):
        start = startIndices[i] - 1
        end = endIndices[i] - 1
        while start < end and s[start] != '|':
            start += 1
        while start < end and s[end] != '|':
            end -= 1
        ans.append(mem[end] - mem[start])
    return ans

    # ans = []
    # for idx, i in enumerate(startIndices):
    #     start = i - 1
    #     end = endIndices[idx]
    #     substring = s[start:end]
    #     mem = []
    #     print(substring)
    #     for ch in substring:
    #         if ch == '|':
    #             mem.append(0)
    #         elif mem:
    #             mem[-1] += 1
    #     if mem:
    #         mem.pop()
    #     ans.append(sum(mem))
    # return ans

if __name__ == "__main__":
    # n = 5
    # arr = [3, 7, 5, 6, 2]
    # print(minimalHeaviestSetA(arr))
    s = '|**|*|*'
    startIndices = [1, 1, 2]
    endIndices = [5, 6, 6]
    print((numberOfItems(s, startIndices, endIndices)))
