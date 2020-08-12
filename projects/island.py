islands =  [[0,1,0,1,0],
            [1,1,0,1,1],
            [0,0,0,0,0],
            [1,0,0,1,0],
            [1,1,0,1,0],
            ]

class Stack():
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None
    def size(self):
        return len(self.stack)

def island_counter(islands):
    row_count = len(islands)
    col_count = len(islands[0])
    visited = []

    # create visited
    for _ in range(row_count):
        visited.append([False] * len(islands[0]))
    
    island_count = 0

    for row in range(row_count):
        for col in range(col_count):

            if not visited[row][col]:
                if islands[row][col] == 1:

                #Traverse and mark each as visited
                    dft(row, col, islands, visited)

                #increment counter
                    island_count += 1
    return island_count

def dft(row, col, islands, visited):
    s = Stack()

    s.push((row,col))

    while s.size() > 0:
        r, c = s.pop()

        if not visited[r][c]:
            visited[r][c] = True

            for neighbor in get_neighbors(r, c, islands):
                s.push(neighbor)

def get_neighbors(row, col, islands):
    row_count = len(islands)
    col_count = len(islands[0])

    neighbors = []

    if row > 0 and islands[row-1][col] == 1:
        neighbors.append((row-1, col))

    if row < row_count-1 and islands[row+1][col] == 1:
        neighbors.append((row+1, col))

    if col > 0 and islands[row][col-1] == 1:
        neighbors.append((row, col-1))

    if col < col_count-1 and islands[row][col+1] == 1:
        neighbors.append((row, col+1))
    return neighbors



print(island_counter(islands))

