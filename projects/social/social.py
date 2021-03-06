import random

class User:
    def __init__(self, name):
        self.name = name

class SocialGraph:
    def __init__(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}

# class Queue():
#     def __init__(self):
#         self.queue = []
#     def enqueue(self, value):
#         self.queue.append(value)
#     def dequeue(self):
#         if self.size() > 0:
#             return self.queue.pop(0)
#         else:
#             return None
#     def size(self):
#         return len(self.queue)

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            print("WARNING: You cannot be friends with yourself")
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

    def populate_graph(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME

        # Add users
        for i in range(num_users):
            self.add_user(f'User {i}')

        # Create friendships
        possible_friendships = []
        for user_id in self.users:
            for friend_id in range(user_id + 1, self.last_id+1):
                possible_friendships.append((user_id, friend_id))

        #shuffle possible friendships
        random.shuffle(possible_friendships)

        #because each friendship makes bi-directional, must divide by 2
        for i in range(num_users * avg_friendships // 2):
            friendship  = possible_friendships[i]
            self.add_friendship(friendship[0], friendship[1])

    def get_all_social_paths(self, user_id, friendships):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        #visited = {}  # Note that this is a dictionary, not a set
        print(friendships)
        results = {user_id:[user_id]}
        arr = []
        visited = [user_id]
        arr.append(user_id)
        while len(results) < len(friendships):
            current = arr.pop(0)
            # make key/ array
            for i in friendships[current]:
                if i not in visited:
                    # make new unrelated arr python
                    addArr = results[current][:]
                    # add its value to the arr
                    addArr.append(i)
                    # add to results
                    results[i]=addArr
                #put in arr
                if i not in visited:
                    arr.append(i)
                    visited.append(i)
                #print('results', results , 'arr', arr, 'visited', visited)
               
        return results
            #break
            # results[current] = [current]
            # visited.append(current)
            # print(results)
            

        
        # !!!! IMPLEMENT ME
        return visited

# print(get_all_social_paths(1))


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(10, 2)
    #print(sg.friendships)
    connections = sg.get_all_social_paths(1, sg.friendships)
    print(connections)
