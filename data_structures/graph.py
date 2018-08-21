class Graph:
    """ A graph implemented using adjency lists (dict of sets) """

    def __init__(self, graph={}):
        self._adjecents = graph
    
    # TODO: Go through 'adjacents' and 2way bind?
    def add_node(self, node, adjacents):
        if node in self._adjecents:
            self._adjecents[node].add(adjacents)
        else:
            self._adjecents[node] = set(adjacents)
    
    def remove_node(self, node):
        _ = self._adjecents.pop(node)
    
    def bfs(self, start):
        # Initialize visited list
        path, visited, q = [], set(), [start] 
        while q:
            current_node = q.pop(0)
            if current_node not in visited:
                path.append(current_node)
                visited.add(current_node)
                q.extend(self._adjecents[current_node] - visited)
        return path

    def __str__(self):
        return "{}".format(self._adjecents)
    
    def __repr__(self):
        return repr(self._adjecents)