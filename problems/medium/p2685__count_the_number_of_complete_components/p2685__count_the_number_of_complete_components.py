class Solution:
    def countCompleteComponents(self, n: int, edges: list[list[int]]) -> int:
        count = 0
        vertices_edges: dict[int, set] = {i: set() for i in range(n)}
        for v1, v2 in edges:
            vertices_edges[v1].add(v2)
            vertices_edges[v2].add(v1)
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
