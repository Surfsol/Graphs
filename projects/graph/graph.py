"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
      
        # add empty set
        self.vertices[vertex_id] = set()
     

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        
        #.add adds to a set
        self.vertices[v1].add(v2)
     
        

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        #find edges that connect to vertex
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # make a queue
        q = Queue()
        # enqueue our starting node
        q.enqueue(starting_vertex)
        # make a set to track if been before
        visited = set()
        # while in que not empty
        while q.size() > 0:
        # dequeue whatever at the front of line, current node
            current_node = q.dequeue()
        # if we haven't visited this node yet
            if current_node not in visited:
        # mark as visited
                visited.add(current_node)
        # print the vertex
        # get its neighbors
                neighbors = self.get_neighbors(current_node)
        # for each of neighbors add to que
                for neighbor in neighbors:
                    q.enqueue(neighbor)
        
        





    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # use a stack
        s = Stack()
        # push on starting node
        s.push(starting_vertex)
        # make a set to track if been there before
        visited = set() 
        # while stack not empty
        while s.size():
        # pop off top of stack, this is current_node
            current_node = s.pop()
        # if have not visited before, mark as visited
            if current_node not in visited:
                visited.add(current_node)
        # Add neighbors to top of stack
                neighbors = self.get_neighbors(current_node)
                for neighbor in neighbors:
                    s.push(neighbor)

    def dft_recursive(self, starting_vertex, visited=set()):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        #mark vertex as visited
        visited.add(starting_vertex)
        print(starting_vertex)
        # for each neighbor
        neighbors = self.get_neighbors(starting_vertex)
        # if not visited 
        for neighbor in neighbors:
            if neighbor not in visited:
                # recurse
                self.dft_recursive(neighbor, visited)
        
      

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # make a queue
        q = Queue()
        # insert starting_vertex
        visited = set()
        # need to return shortest path
        path = [starting_vertex]
        q.enqueue(path)
        # while q is not empty
        while q.size() > 0:
            #take out the q and put in path
            current_path = q.dequeue()
            #current node is last one in current path
            current_node = current_path[-1]
            #if current_node = destination, then retur
            if current_node == destination_vertex:
                return current_path
        # if not visited
            if current_node not in visited:
                visited.add(current_node)
                #get neighbors
                neighbors = self.get_neighbors(current_node)
                #for each neighbor
                for neighbor in neighbors:
                    #copy path, not to mutate original
                    path_copy = current_path[:]
                    path_copy.append(neighbor)
                    #add to que
                    q.enqueue(path_copy)
            
    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        pass  # TODO

    def dfs_recursive(self, vertex, destination_vertex, visited=set(), path):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.

        """
        #mark out node as visited
        visited.add(vertex)
        #check if target node. if so return path
        if vertex == destination_vertex:
            return path
        if len(path) == 0:
            path.append(vertex)

        neighbors = self.get_neighbors(vertex)
        for  neighbor in neighbors:
            #check if visited
            if neighbor not in visited:
                result = self.dfs_recursive(neighbor, destination_vertex, path + [neighbor])
                if result is not None:
                    return result
        
        
  

if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
