def minTrioDegree(n: int, edges: list[list[int]]) -> int:
    adj = [[False] * (n + 1) for _ in range(n + 1)]
    degree = [0] * (n + 1)

    for u, v in edges:
        adj[u][v] = True
        adj[v][u] = True
        degree[u] += 1
        degree[v] += 1

    best = float("inf")

    for u in range(1, n + 1):
        neighbors_u = adj[u]
        for v in range(u + 1, n + 1):
            if not neighbors_u[v]:
                continue

            neighbors_v = adj[v]
            pair_degree = degree[u] + degree[v]

            for w in range(v + 1, n + 1):
                if neighbors_u[w] and neighbors_v[w]:
                    trio_degree = pair_degree + degree[w] - 6
                    if trio_degree == 0:
                        return 0
                    if trio_degree < best:
                        best = trio_degree

    return -1 if best == float("inf") else best