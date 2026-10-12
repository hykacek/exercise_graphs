#TASK 1
def build_adjacency_list(edges, directed=False):
    graph = {}
    for u, v in edges:
        if u not in graph:
            graph[u] = []
        if v not in graph:
            graph[v] = []
    for u, v in edges:
        graph[u].append(v)
        if not directed:
            graph[v].append(u)
    return graph

def degrees(graph):
    degree_dict = {}
    for v in graph:
        degree_dict[v] = len(graph[v])
    return degree_dict

def in_out_degree(graph):
    in_degree = {v: 0 for v in graph}
    out_degree = {v: 0 for v in graph}
    for v in graph:
        out_degree[v] = len(graph[v])
        for neighbor in graph[v]:
            if neighbor not in in_degree:
                in_degree[neighbor] = 0
            in_degree[neighbor] += 1
    return in_degree, out_degree

edges = [("P1", "P2"), ("P1", "P3"), ("P2", "P3"), ("P3", "P4"), ("P4", "P5")]

