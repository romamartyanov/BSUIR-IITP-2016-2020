import numpy as np
from ford import ford
from pprint import pprint

def build_pairs(costs: np.ndarray):
        n, m = costs.shape
        graph = []
        for i in range(n):
            for j in range(m):
                if costs[i][j] == 0:
                    graph.append((i + 1, j + n + 1, 1))
        for i in range(n, 2 * n):
            graph.append((i + 1, 2 * n + 1, 1))
        for i in range(n):
            graph.append((0, i + 1, 1))

        return graph

class Assignments:
    def first_costs_transform(self, costs):
        n, m = costs.shape
        for i in range(n):
            costs[i, :] -= np.min(costs[i, :])
        for i in range(m):
            costs[:, i] -= np.min(costs[:, i])

        return costs

    def step2(self, flow, costs, L):
        n, m = costs.shape

        N1 = np.array([i for i in range(n) if i + 1 in L], dtype=np.int)
        N2 = [i for i in range(n) if i + n + 1 in L]
        N2_inv = np.array(list(set(range(n)) - set(N2)), dtype=np.int)

        с = costs[N1, :]
        с = с[:, N2_inv]
        alpha = np.min(с)

        for i in range(n):
            for j in range(m):
                if i in N1 and j not in N2:
                    costs[i, j] -= alpha
                if i not in N1 and j in N2:
                    costs[j, i] += alpha

        return costs

    def prepare_answer(self, flow, costs, n):
        ans = []
        total_cost = 0

        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if flow.get(i, {}).get(j + n, 0) != 1: continue
                
                ans.append(j - 1)
                total_cost += costs[i - 1, j - 1]

        return ans, total_cost

    def solve(self, costs):
        src_costs = costs.copy()
        n, _ = costs.shape

        costs = self.first_costs_transform(costs)

        print('Costs matrix after first transform')
        print(costs)

        while True:
            graph = build_pairs(np.array(costs))
            max_flow, current_flow, L = ford(graph, 0, 2*n+1)

            print('Max flow: ', max_flow)
            pprint(current_flow)
            
            if max_flow == n:
                return self.prepare_answer(current_flow, src_costs, n)

            costs = self.step2(current_flow, costs, L)            
