
def find_ladders(begin_word, end_word):
    q = Queue()
    visited = set()

    q.enqueue([begin_word])
    while q.size() > 0:
        path = q.dequeue()
        v = path[-1]

        if v not in visited:
            visited.add(v)
            if v == end_word:
                return path
            
            for neighbor in get_neighbors(v):
                path_copy = list(path)
                path_copy.append(neighbor)
                q.enqueue


