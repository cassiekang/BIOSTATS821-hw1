"""Create complicated graphs"""
def add_layer(graph: dict[str,set[str]], layer_idx:int, num_nodes:int):
    previous_nodes = {key for key in graph if key.startswith (f"{layer_idx-1}")}
    print(previous_nodes)

    new_nodes = set(f"{layer_idx}.{node_idx}" for node_idx in range(num_nodes))
    print(new_nodes)

    for new_node in new_nodes:
        graph[new_node] = set()
        for previous_node in previous_nodes:
            graph[previous_node].add(new_node)
    return graph

if __name__ == "__main__":
   # graph = {"0", {"1.1","1.2"}, "1.1": set(), "1.2": set()}
    graph = {"0":set()}
    graph = add_layer(graph, 1, 500)
    graph = add_layer(graph, 2, 500)
    graph = add_layer(graph, 3, 500)
