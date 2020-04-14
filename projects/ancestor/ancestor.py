
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

def earliest_ancestor(ancestors, starting_node):
    pass