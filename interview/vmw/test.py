#!/usr/bin/env python
# coding=utf-8
from math import sqrt


def divide_wood(n, m, s):
    if n % 2 == 0:
        return 'B'
    for i in range(2, int(sqrt(m)) + 1):
        if m % i == 0 and (i > s or m / i > s):
            return 'A'
    return 'B'


def pick_number(num_list):
    n = len(num_list)
    a_list = [0] * n
    b_list = num_list
    gamer_list = [a_list, b_list]
    flip = [0, 1]
    for step in range(1, n):
        temp_list = [[], []]
        for l in range(0, n - step):
            r = l + step
            st = num_list[l] + gamer_list[flip[0]][l + 1]
            nd = num_list[r] + gamer_list[flip[0]][l]
            if st >= nd:
                temp_list[flip[0]].append(st)
                temp_list[flip[1]].append(gamer_list[flip[1]][l + 1])
            else:
                temp_list[flip[0]].append(nd)
                temp_list[flip[1]].append(gamer_list[flip[1]][l])
        gamer_list[0] = temp_list[0]
        gamer_list[1] = temp_list[1]
        tmp = flip[0]
        flip[0] = flip[1]
        flip[1] = tmp
    return gamer_list[n % 2][0]


def delete_graph2(n, graph):
    cnt = 0
    in_list = [0] * (n + 1)
    for edge in graph:
        in_list[edge[1]] += 1

    children = {}
    for i in range(1, n + 1):
        children[i] = list()
    for edge in graph:
        children[edge[0]].append(edge[1])

    while children:
        del_list = list()
        try:
            in_zero = in_list.index(0, 1)
        except ValueError:
            break

        del_list.append(in_zero)
        in_list[in_zero] = -1
        for child in children[in_zero]:
            if child in children.keys():
                del_list.append(child)
                in_list[child] = -1
                for grandchild in children[child]:
                    in_list[grandchild] -= 1
                children.pop(child)
        children.pop(in_zero)
        cnt += 1
        # time.sleep(1)
    return cnt
    

n = int(raw_input())
S = raw_input()
num_list = []
for i in S.split(" "):
    num_list.append(int(i))
print pick_number(num_list)

# divide wood
# ans = []
# T = int(raw_input())
# for i in range(T):
#     S = raw_input()
#     n = int(S.split(" ")[0])
#     m = int(S.split(" ")[1])
#     s = int(S.split(" ")[2])
#     ans.append(divide_wood(n, m, s))
# 
# print ans
    
# delete graph
# S = raw_input()
# n = int(S.split(" ")[0])
# m = int(S.split(" ")[1])
# node_list = list()
# for i in range(m):
#     tmp_list = list()
#     S = raw_input()
#     tmp_list.append(int(S.split(" ")[0]))
#     tmp_list.append(int(S.split(" ")[1]))
#     node_list.append(tmp_list)
# 
# print delete_graph2(n, node_list)
