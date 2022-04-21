class Stack:

    def __init__(self):
        self.list = []

    def push(self, item):
        self.list.append(item)

    def pop(self):
        return self.list.pop()

    def top(self):
        return self.list[-1]

    def is_empty(self):
        return len(self.list) == 0


def depth_first_search(graph, start):
    stack = Stack()
    stack.push(start)
    path = []

    while not stack.is_empty():
        vertex = stack.pop()
        if vertex in path:
            continue
        path.append(vertex)
        for neighbor in graph[vertex]:
            stack.push(neighbor)

    return path


def main():
    adjacency_matrix = {
        'S' : ['A','B','C'],
    'A' : ['S','D'],
    'B' : ['D','S'],
    'C' : ['D','S'],
    'D' : ['A','B','C']
    }
    dfs_path = depth_first_search(adjacency_matrix, 'B')
    print("Depth First Traversal is : ")
    print(dfs_path)


if __name__ == '__main__':
    main() 