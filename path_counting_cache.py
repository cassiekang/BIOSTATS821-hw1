"""Path counting example."""

cache: dict[str,int] = dict()

def count_paths(edges: dict[str,set[str]],start:str,end:str) -> int: # f(N,L)
  """"Count paths.
  
  time complexity without caching: O(N^L)
  """
  question = start
  if question in cache:
    return cache[question]
  
  if start == end:
   return 1
  can_get_to = edges[start]
  num_paths = 0
  for node in can_get_to: # N times
    num_paths += count_paths(edges,node,end) # f(N,L-1)

  cache[question] = num_paths
  return num_paths

if __name__=="__main__":
    edges: dict[str,set[str]]={
    "a":{"b","c"},
    "b":{"c","d"},
    "c":{"d","e"},
    "d": set(),
    "e":set(),
}

print(count_paths(edges,"a","d"))