import numpy as np


class Dijkstra:
    def __init__(self, pairs, n):
        """
        Create graph for dijkstra algorithm

        :param pairs:
        :return:
        """

        self.nodes_count = n
        self.graph = [[] for _ in range(n)]
        for rib, rib_weight in pairs:
            self.graph[rib[0] - 1].append((rib[1] - 1, rib_weight))

    def __find_next_node(self, d, used):
        """
        Find next node with min weight

        :param d:
        :param used:
        :return:
        """

        # находим лучшую следующую проверяемую точку
        # проверяемой точке присваиваем максимальный вес
        cur_node = [np.inf, 0]
        # текущая позиция проверки
        # cur_position = 0
        for i in range(self.nodes_count):
            if d[i] < cur_node[0] and not used[i]:
                # если мы в ней еще не были и ее вес меньше текущего, то
                cur_node = [d[i], i]
        return cur_node, d, used

    def solve(self, start_node):
        """
        Дан взвешенный ориентированный[1] граф G(V,E) без дуг отрицательного веса
        Найти кратчайшие пути от некоторой вершины a графа G до всех остальных вершин этого графа.

        :param start_node:
        :return:
        """
        # вектор с минимальными стоимостями перемещения до вершин
        # заполняем вектор длинн пути размером n (кол-во точек в графе) максимальными значени
        d = np.full((self.nodes_count,), np.inf)
        # вектор посещенных точек
        used = np.full((self.nodes_count,), False)
        # точка, с которой начинаем путь, стоимость перещемения в нее - 0
        d[start_node] = 0
        for i in range(self.nodes_count):
            cur_node, d, used = self.__find_next_node(d, used)
            # помечаем лучшую точку, как проверенную
            used[cur_node[1]] = True
            # смотрим с кем она граничит и находим минимум стоимости перемещения в них
            for point_to, weight in self.graph[cur_node[1]]:
                d[point_to] = min(d[point_to], cur_node[0] + weight)
        return list(d)
