import numpy as np


class MaxPath:
    def __init__(self, pairs, start_node, end_node, n):
        self.start_node = start_node - 1
        self.end_node = end_node - 1

        self.b = np.full((n,), 0)
        self.f = np.full((n,), -1)
        self._i = {self.start_node}

        self.graph = [[] for _ in range(n)]
        for rib, rib_weight in pairs:
            self.graph[rib[0] - 1].append((rib[1] - 1, rib_weight))

    def __get_connected_nodes(self, source, rule):
        nodes = []
        for end_point, _ in self.graph[source]:
            if rule(end_point):
                nodes.append(end_point)
        return nodes

    def __get_parents(self, node):
        parents = []
        for from_node, end_points in enumerate(self.graph):
            for end_point, weight in end_points:
                if end_point == node:
                    parents.append((from_node, weight))
                    break
        return parents

    def __get_parent_ids(self, node):
        return list(map(lambda x: x[0], self.__get_parents(node)))

    def __is_in_i(self, nodes):
        for node in nodes:
            if node not in self._i:
                return False
        return True

    def __step(self):
        nodes = set()

        for x in self._i:
            connected_with_x = self.__get_connected_nodes(
                x, lambda q: q not in self._i)
            nodes = nodes.union(connected_with_x)

        found_connected_nodes = []
        for node in nodes:
            node_parents = self.__get_parent_ids(node)
            if self.__is_in_i(node_parents):
                found_connected_nodes.append(node)

        return found_connected_nodes

    def __get_path(self):
        path = []
        while self.f[self.end_node] != -1:
            self.end_node = self.f[self.end_node]
            path.append(self.end_node)
        return path

    def find_max_path(self):
        while True:
            connected_nodes = self.__step()
            
            if len(connected_nodes) != 0:
                for node in connected_nodes:
                    node_inputs = self.__get_parents(node)
                    for input_node, weight in node_inputs:
                        if self.b[node] < self.b[input_node] + weight:
                            self.b[node] = self.b[input_node] + weight
                            self.f[node] = input_node
                    self._i.add(node)
            else:
                break

        end_b = self.b[self.end_node]
        end_f = self.__get_path()

        return end_b, end_f
