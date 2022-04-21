from queue import Queue

graph = {
    0 : [1,2,3],
    1 : [0,4],
    2 : [0,4],
    3 : [0,4],
    4 : [1,2,3]
    }
print("The adjacency List representing the graph is:")
print(graph)
 
 
def bfs(graph, source):
    Q = Queue()
    visited_vertices = set()
    Q.put(source)
    visited_vertices.update({1})
    while not Q.empty():
        vertex = Q.get()
        print(vertex, end="  ")
        for u in graph[vertex]:
            if u not in visited_vertices:
                Q.put(u)
                visited_vertices.update({u})
 
print("BFS traversal of graph with source 1 is:")
bfs(graph, 1)