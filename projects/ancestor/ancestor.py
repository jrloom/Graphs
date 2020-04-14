
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
    pass