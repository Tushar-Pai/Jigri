def dfs(source, goal, vis, limit):
    if source == goal:
        print("Success")
        return True
    if limit <= 0:
        return False
    print(source)
    vis.append(source)
    poss_move = possible_moves(source, vis)
    for move in poss_move:
        if dfs(move, goal, vis, limit - 1):
            return True
    return False


def possible_moves(source, vis):
    b = source.index(-1)
    dir = []
    if b not in [0, 1, 2]:
        dir.append('u')
    if b not in [0, 3, 6]:
        dir.append('l')
    if b not in [2, 5, 8]:
        dir.append('r')
    if b not in [6, 7, 8]:
        dir.append('d')
    possible_move = []
    poss_move = []
    for d in dir:
        possible_move.append(gen(source, b, d))
        for move in possible_move:
            if move not in vis:
                poss_move.append(move)
    return poss_move


def gen(source, b, d):
    temp = source.copy()
    if d == 'u':
        t = temp[b - 3]
        temp[b - 3] = temp[b]
        temp[b] = t
    elif d == 'd':
        temp[b + 3], temp[b] = temp[b], temp[b + 3]
    elif d == 'r':
        temp[b + 1], temp[b] = temp[b], temp[b + 1]
    else:
        temp[b - 1], temp[b] = temp[b], temp[b - 1]
    return temp


def iddfs(source, goal, depth):
    for i in range(depth):
        vis = []
        if dfs(source, goal, vis, i+1):
            print("Found At depth: ", i+1)
            return
        print("Not Found At depth : ", i+1)
    print("Not Found At depth : ", depth)
    return


source = [1, 2, 3, -1, 4, 5, 6, 7, 8]
goal = [1, 2, 3, 4, 5, -1, 6, 7, 8]
depth = 9
iddfs(source, goal, depth)
