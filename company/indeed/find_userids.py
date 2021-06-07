"""
Given a collection of actions and userIds, an error occurs when a userId takes
a specific action in order for example,

A => B => C : This sequence of actions yields error

Write a function that takes in a list of (Actions, UserIds) pairs and returns the user Id that ecounters the error

Sample Input:

action_user_1 = [
["A", "1"], <- A(1)
["B", "1"], <- B(1)
["B", "2"],
["C", "1"], <- C(1)
["C", "2"],
["C", "3"],
["A", "2"],  <- A(2)
["A", "3"],
["A", "2"],
["B", "2"],  <- B(2)
["C", "2"], <- C(2)
]

Error action -> ["ABC"]
Expected output -> [1,2]

action_user_2 = [
["A", "1"],
["A", "1"]
["A", "1"]
["B", "1"],
["B", "2"], <- B
["C", "2"],
["C", "2"],
["C", "3"],
["A", "2], <- A
["A", "3"],
["A", "2"],
["B", "2],
["C", "2"], <- C
]

Error action -> ["BAC"]
Expected output -> [2]
"""


from collections import defaultdict


def find_userids(actions, error_string):
    result = []
    user_id_actions = defaultdict(list)

    for action, userid in actions:
        user_id_actions[userid].append(action)
    print(',user_id_actions',user_id_actions)
    for userid, actions in user_id_actions.items():

        count = ''.join(actions).count(error_string)
        print('count',actions,''.join(actions),count)
        if count:
            result.append(userid)

    return result


def user_errors(actions):
    data = dict()
    list_of_error_users = []
    verify_order = []
    for user_action in actions:
        if user_action[1] not in data:
            data[user_action[1]] = [user_action[0]]
        else:
            data[user_action[1]].append(user_action[0])

    for id, actions in data.items():
        if len(actions) >= 2:
            for index in range(len(actions) - 1):
                if abs(ord(actions[index]) - ord(actions[index + 1])) == 1:
                    verify_order.append(actions[index])
                    if len(verify_order) >= 2:
                        list_of_error_users.append(id)
                        break
    return list_of_error_users


action_user_1 = [
    ["A", "1"],
    ["B", "1"],
    ["B", "2"],
    ["C", "1"],
    ["C", "2"],
    ["C", "3"],
    ["A", "2"],
    ["A", "3"],
    ["A", "2"],
    ["B", "2"],
    ["C", "2"],
]

print(find_userids(action_user_1, "ABC"))
# print(user_errors(action_user_1))
