class Solution:
    def countCompleteComponents(self, n: int, edges: list[list[int]]) -> int:
        vertices_edges: dict[int, set] = dict()
        count = 0
        for i in range(n):
            vertices_edges[i] = set()
        for edge in edges:
            vertices_edges[edge[0]].add(edge[1])
            vertices_edges[edge[1]].add(edge[0])
        checked = set()
        for vertex in vertices_edges:
            if vertex in checked:
                continue
            current_neighbors = vertices_edges[vertex]
            if not current_neighbors:
                count += 1
                continue
            complete = True
            checked.update(current_neighbors | {vertex})
            for neighbor in current_neighbors:
                neighbor_neighbors = vertices_edges[neighbor]
                different_neighbors = neighbor_neighbors.difference({vertex})\
                    ^ current_neighbors.difference({neighbor})
                complete = complete and not different_neighbors
                checked.update(different_neighbors)
            if complete:
                count += 1

        return count
