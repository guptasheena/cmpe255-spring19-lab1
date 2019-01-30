import operator

users = [
    {"id": 0, "name": "Hero"},
    {"id": 1, "name": "Dunn"},
    {"id": 2, "name": "Sue"},
    {"id": 3, "name": "Chi"},
    {"id": 4, "name": "Thor"},
    {"id": 5, "name": "Clive"},
    {"id": 6, "name": "Hicks"},
    {"id": 7, "name": "Devin"},
    {"id": 8, "name": "Kate"},
    {"id": 9, "name": "Klein"}
]

friendship = [
    (0, 1),
    (0, 2),
    (1, 2),
    (1, 3),
    (2, 3),
    (3, 4),
    (4, 5),
    (5, 6),
    (6, 7),
    (6, 8),
    (7, 8),
    (8, 9)
]


def num_friends(user):
    '''
    Find number of friends for a given user
    '''
    count = 0
    for index in friendship:
        if index[0] == user["id"]:
            count = count + 1

    print("The number of friends of " +
          str(user["name"]) + " is: " + str(count))
    return count


def sort_by_num_friends():
    '''
    Sort from "most friends" to "least friends"
    '''
    number_of_friends = {}
    for user in users:
        number_of_friends[user["id"]] = num_friends(
            {"id": user["id"], "name": user["name"]})

    sorted_number_of_friends = sorted(number_of_friends.items(),
                                      key=operator.itemgetter(1), reverse=True)

    for index in range(len(sorted_number_of_friends)):
        print(str(users[sorted_number_of_friends[index][0]]
                  ["name"]) + " has " + str(sorted_number_of_friends[index][1]) + " friends.")


'''
method invocations
'''
sort_by_num_friends()

num_friends({"id": 0, "name": "Hero"})
num_friends({"id": 1, "name": "Dunn"})
num_friends({"id": 2, "name": "Sue"})
num_friends({"id": 3, "name": "Chi"})
num_friends({"id": 4, "name": "Thor"})
num_friends({"id": 5, "name": "Clive"})
num_friends({"id": 6, "name": "Hicks"})
num_friends({"id": 7, "name": "Devin"})
num_friends({"id": 8, "name": "Kate"})
num_friends({"id": 9, "name": "Klein"})
