"""Path counting example."""

def count_paths(edges:dict[str,set[str]], start: str, end: str) -> int: #f(N,L)
    """Count paths."""
    if start == end:
        return 1
    can_get_to = edges[start]
    num_paths = 0
    for node in can_get_to: # N times
        num_paths += count_paths(edges, node, end) # f(N, L-1)
    return num_paths

if __name__ == "__main__":
    edges: dict[str,set[str]] = {
        "a": {"b", "c"}, #you can get to b or c from a
        "b": {"c", "d"}, #you can get to d from b
        "c": {"d", "e"}, # you can get to d from class
        "d":  set()      
     }
    