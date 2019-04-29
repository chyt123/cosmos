import collections
import time
from math import sqrt


class Graph(object):
    def __init__(self, n, node_list):
        self.node_list = node_list
        self.node_edge = {}
        self.node_edge_r = {}
        self.cnt = 0
        for i in range(n):
            self.node_edge[i + 1] = set([])
            self.node_edge_r[i + 1] = set([])
        self.add_node_list()
        
    def add_node_list(self):
        for node_edge_list in self.node_list:
            self.add_node_edge(node_edge_list)
        
    def add_node_edge(self, node_edge_list):
        self.node_edge[node_edge_list[0]].add(node_edge_list[1])
        self.node_edge_r[node_edge_list[1]].add(node_edge_list[0])
        
    def find_in_zero_node(self):
        # in_nodes = set([])
        # for node in self.node_edge.values():
        #     in_nodes = in_nodes.union(node)
        # for node in self.node_edge.keys():
        #     if node not in in_nodes:
        #         return node
        # return None
        for node, value in self.node_edge_r.items():
            if not value:
                return node
        return None
    
    def delete_given_ele(self, ele, d): 
        d.pop(ele)
        for value in d.values():
            value.discard(ele)
    
    def delete_nodes(self):
        while self.node_edge:
            in_zero_node = self.find_in_zero_node()
            if in_zero_node:
                delete_list = list()
                for i in self.node_edge[in_zero_node]:
                    delete_list.append(i)
                for i in delete_list:
                    self.delete_given_ele(i, self.node_edge)
                    self.delete_given_ele(i, self.node_edge_r)
                self.delete_given_ele(in_zero_node, self.node_edge)
                self.delete_given_ele(in_zero_node, self.node_edge_r)
                self.cnt += 1
            time.sleep(1)
        return self.cnt 
        
        
class Solution(object):
    def divide_wood(self, n, m, s):
        if n % 2 == 0:
            return 'B'
        for i in range(s + 1, m):
            if m % i == 0:
                return 'A'
        return 'B'
    
    def pick_number(self, num_list):
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
    
    def delete_graph(self, n, graph):
        g = Graph(n, graph)
        return g.delete_nodes()
    
    def delete_graph2(self, n, graph):
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
        print cnt


if __name__ == "__main__":
    sol = Solution()
    
    # divide wood
    (n, m, s) = (1, 9, 4)
    # print sol.divide_wood(n, m, s)
    
    # pick number
    num_list = [2, 1, 4, 3, 5, 1]
    # print sol.pick_number(num_list)

    # delete_graph
    graph = [
        [1, 2],
        [2, 3],
        [3, 4],
        # [1, 3],
        # [2, 4],
        # [1, 5],
        # [5, 7],
        # [4, 6],
        # [7, 6]
    ]
    print sol.delete_graph2(4, graph)

