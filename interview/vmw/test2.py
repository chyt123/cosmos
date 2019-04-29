#!/usr/bin/env python
# coding=utf-8

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
    
# delete graph
S = raw_input()
n = int(S.split(" ")[0])
m = int(S.split(" ")[1])
node_list = list()
for i in range(m):
    tmp_list = list()
    S = raw_input()
    tmp_list.append(int(S.split(" ")[0]))
    tmp_list.append(int(S.split(" ")[1]))
    node_list.append(tmp_list)

print delete_graph2(n, node_list)
