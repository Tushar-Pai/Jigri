
# Test 1
src = [1, 2, 3, -1, 4, 5, 6, 7, 8]
target = [1, 2, 3, 4, 5, -1, 6, 7, 8]

def display(state):
    for i in range(9):
        if(i%3==0):print('')
        print(state[i],end="  ")
    print("\n---------") 


def generateState(cur, visited_states):

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

    return [state for state in states if state not in visited_states]


# Generate move for given direction
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


def bfs(src, target):
    queue = []
    queue.append(src)
    vis = []

    while len(queue) > 0:
        source = queue.pop(0)
        vis.append(source)
        display(source)

        if source == target:
            print("success")
            return

        
        states = generateState(source, vis)

        for state in states:
            if state not in vis and state not in queue:
                queue.append(state)

bfs(src, target)
# # Test 2
# src = [1,2,3,-1,4,5,6,7,8]
# target=[1,2,3,6,4,5,-1,7,8]
#
#
#
# bfs(src, target)