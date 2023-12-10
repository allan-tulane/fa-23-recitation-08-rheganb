from collections import deque
from heapq import heappush, heappop 

def shortest_shortest_path(graph, source):
    """
    Params: 
      graph.....a graph represented as a dict where each key is a vertex
                and the value is a set of (vertex, weight) tuples (as in the test case)
      source....the source node
      
    Returns:
      a dict where each key is a vertex and the value is a tuple of
      (shortest path weight, shortest path number of edges). See test case for example.
    """
    ### TODO
    def shortest_shortest_path_recursive(visited, frontier):
      if len(frontier) == 0:
        return visited
      else:
        distance_weight, edges, node = heappop(frontier)
        if node in visited:
          return shortest_shortest_path_recursive(visited, frontier)
        else:
          visited[node] = (distance_weight, edges)
          for neighbor, weight in graph[node]:
            heappush(frontier, (distance_weight + weight, edges + 1, neighbor))
          return shortest_shortest_path_recursive(visited, frontier)

    frontier = []
    heappush(frontier, (0, 0, source))
    visited = dict()
    return shortest_shortest_path_recursive(visited, frontier)
        
    

    
    
def bfs_path(graph, source):
    """
    Returns:
      a dict where each key is a vertex and the value is the parent of 
      that vertex in the shortest path tree.
    """
    def bfs_path_recursive(visited, frontier, parent):
      if len(frontier) == 0:
        return parent
      else:
        node = frontier.popleft()
        visited.add(node)
        for i in graph[node]:
          if i not in visited:
            frontier.append(i)
            parent[i] = node
        return bfs_path_recursive(visited, frontier, parent)

def get_sample_graph():
     return {'s': {'a', 'b'},
            'a': {'b'},
            'b': {'c'},
            'c': {'a', 'd'},
            'd': {}
            }


    
def get_path(parents, destination):
    """
    Returns:
      The shortest path from the source node to this destination node 
      (excluding the destination node itself). See test_get_path for an example.
    """
    if destination in parents:
      return get_path(parents, parents[destination] + parents[destination])
    else:
      return destination

