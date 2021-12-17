src = [1, 2, 3, -1, 4, 5, 6, 7, 8]
target = [1, 2, 3, 4, 5, -1, 6, 7, 8]

def display(state):
    for i in range(9):
        if(i%3==0):print('')
        print(state[i],end="  ")
    print("\n---------") 


def generateState(cur):

    i = cur.index(-1)
    moves = []

    if(i%3<2):moves.append('r')
    if(i>2):moves.append('u')
    if(i<6):moves.append('d')
    if(i%3>0):moves.append('l')

    states = []

    for move in moves:
        state=next_state(cur, i, move)
        states.append(state)

    return states


def next_state(cur,i,move):
    temp=cur[:]
    if(move=='r'):
        temp[i],temp[i+1]=temp[i+1],temp[i]
    if(move=='l'):
        temp[i],temp[i-1]=temp[i-1],temp[i]
    if(move=='u'):
        temp[i],temp[i-3]=temp[i-3],temp[i]
    if(move=='d'):
        temp[i],temp[i+3]=temp[i+3],temp[i]
    return temp


def h(state, target):
    count=0
    i=0
    for j in state:
        if state[i]!= target[i]:
            count=count+1
    return count

def astar(state,target):# Add inputs if more are required
    states = [src]
    g = 0
    visited_states =[]
    while len(states):
        print(f"Level: {g}")
        moves = []
        for state in states:
            visited_states.append(state)
            display(state)
            if state == target:
                print("Success")
                return
            moves += [move for move in generateState(state) if move not in moves]
        costs = [g + h(move, target) for move in moves]
        states = [moves[i] for i in range(len(moves)) if costs[i] == min(costs)]
        g += 1
    print("Fail")



astar(src, target)