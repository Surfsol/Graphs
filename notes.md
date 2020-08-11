breath first search will return the fastest path

if you can do get neighbors you can treat it like a graph


solving Graph Problems

1. Describe the problem using graphs terminology
    What are your nodes?
    What are nodes connected?
    What are your connected components?

2. Build graph, or write getNeighbors()
    Figure out how to get the node's edges

3. Choose your algorithm, and appy it

Example

Given two words, begin and end words.
and a dictionary of word list,
return the shortest transformation sequence from begin_word to end_word, such that:

Only one letter can be changed at a time.

Each transformed word must exist in the word list.

from util import Queue

word_list = set()
for word in words:
    word_list.add(word.lower())

def get_neighbors(start_word):
    neighbors = []
    #for every letter in the word
    for letter_index in range(len(start_word)):
        word_list = list(start_word)
        word_list(letter_index) = letter

        word = "".join(word_list)

        if word in word_list and word != start_word:
            neighbors.append(word)
    return neighbors

def wordLatter(start, end):
    q = Queue()
    visited = set()

    q.enqueue([start_word])

    while q.size() > 0:
        current_path = q.dequeue()
        current_word = current_path[-1]

        if current_word == end_word:
            return current_path
        
        if current_word not in visited:
            visited.add(current_word)

            neighbors = get_neighbors(current_word)

            for neighbor in neighbors:
                new_path = current_path + [neighbor]
                q.enqueue(new_path)
