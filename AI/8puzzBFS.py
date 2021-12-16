def print_grid(src):
    state = src.copy()
    state[state.index(-1)] = ' '
    print(
        f"""
{state[0]} {state[1]} {state[2]}
{state[3]} {state[4]} {state[5]}
{state[6]} {state[7]} {state[8]}
        """
    )

def bfs(src,target):
    frontier = [src]
    visited_states = set()
    while len(frontier):
        state = frontier.pop(0)
        print_grid(state)
        visited_states.add(tuple(state))
        if state == target:
            print(f"Success")
            return
        for move in possible_moves(state, visited_states):
            if move not in frontier and tuple(move) not in visited_states:
                frontier.append(move)
    print("Fail")

def possible_moves(state, visited_states): 
    b = state.index(-1)  
    d = []
    if b not in [0,1,2]: 
        d += 'u'
    if b not in [6,7,8]:
        d += 'd'
    if b not in [2,5,8]: 
        d += 'r'
    if b not in [0,3,6]: 
        d += 'l'
    pos_moves = []
    for move in d:
        pos_moves.append(gen(state,move,b))
    return [move for move in pos_moves if tuple(move) not in visited_states]

def gen(state, direction, b):
    temp = state.copy()                              
    if direction == 'u':
        temp[b-3], temp[b] = temp[b], temp[b-3]
    if direction == 'd':
        temp[b+3], temp[b] = temp[b], temp[b+3]
    if direction == 'r':
        temp[b+1], temp[b] = temp[b], temp[b+1]
    if direction == 'l':
        temp[b-1], temp[b] = temp[b], temp[b-1]
    return temp

src=[1,2,3,5,6,-1,7,8,4]
tar=[1,2,3,5,8,6,-1,7,4]
bfs(src,tar)
