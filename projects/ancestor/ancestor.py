

def earliest_ancestor(ancestors, starting_node):
    #btf search
    # find starting node
    # determine if it has connections
    # if so, make those connections the current node, and find if they have a connection.
    # when no more connections return the lowest connection
    current = starting_node
    q = [starting_node]
    visited = set()
    
    while len(q) > 0:
        current = q.pop()
        print('current', current)
        visited.add(current)
        for pair in ancestors:
            if current in pair:
                print('pair', pair)
            
                if pair[0] not in visited:
                    q.append(pair[0])
                    print('q = ', q)
    if current == starting_node:
        current = -1
    return current
           

arr = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
starting_node = 2
print(earliest_ancestor(arr, starting_node))