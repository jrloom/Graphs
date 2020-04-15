
class Queue:
    def __init__(self):
        self.store = []

    def size(self):
        return len(self.store)

    def enqueue(self, val):
        self.store.append(val)
    
    def dequeue(self):
        if self.size() > 0:
            return self.store.pop(0)
        else:
            return None

class Graph:
    def __init__(self):
        self.verts = {}

    def add_vert(self, vert_id):
        self.verts[vert_id] = set()
    
    def add_edge(self, v1, v2):
        if v1 in self.verts and v2 in self.verts:
            self.verts[v1].add(v2)
        else:
            print('error adding edge: verts not found')
    
    def get_neighbors(self, vert_id):
        if vert_id in self.verts:
            return self.verts[vert_id]
        else:
            return None

def earliest_ancestor(ancestors, starting_node):
    # bring in/populate Graph
    # graph = Graph()

    # for (parent, child) in ancestors:
    #     # create parent and child vertices
    #     graph.add_vert(child)
    #     graph.add_vert(parent)
    #     # create edges between parents and children
    #     graph.add_edge(child, parent)

    graph = {}
    for pair in ancestors:
        if pair[1] in graph:
            graph[pair[1]].append(pair[0])
        else:
            graph[pair[1]] = [pair[0]]
    
    # bring in/set Queue
    que = Queue()
    que.enqueue([starting_node])
    max_len = 0

    if starting_node not in graph:
        return -1

    while que.size() > 0:
        path = que.dequeue()
        visited = path[-1]

        if visited in graph:
            for i in graph[visited]:
                new_path = list(path)
                new_path.append(i)
                que.enqueue(new_path)

                if new_path == 0:
                    earliest_ancestor = min(earliest_ancestor, i)
                elif len(new_path) > max_len:
                    earliest_ancestor = i
                    max_len = len(new_path)



        # if path[-1] not in visited:
        #     print(f'do stuff - {path[-1]}')
        #     print(f'{visited}')
        #     earliest_ancestor = visited
        #     visited.add(path[-1])

        # for next_vert in graph.get_neighbors(path[-1]):
        #     new_path = list(path)
        #     new_path.append(next_vert)
        #     que.enqueue(new_path)
    
    return earliest_ancestor
