start=[1,2,3,-1,4,5,6,7,8]
end=[1,2,3,4,5,-1,6,7,8]
visited=[]
count=0

def display(state):
    for i in range(9):
        if(i%3==0):print('')
        print(state[i],end=" ")
    print("\n-------")

def next_state(cur,i,move):
    temp=cur[:]
    if(move=='l'):
        temp[i],temp[i-1]=temp[i-1],temp[i]
    if(move=='r'):
        temp[i],temp[i+1]=temp[i+1],temp[i]
    if(move=='u'):
        temp[i],temp[i-3]=temp[i-3],temp[i]
    if(move=='d'):
        temp[i],temp[i+3]=temp[i+3],temp[i]
    return temp


def generate_state(cur):
    moves=[]
    i=cur.index(-1)
    if(i%3<2):moves.append('r')
    if(i>2):moves.append('u')
    if(i<6):moves.append('d')
    if(i%3>0):moves.append('l')

    states=[]
    for move in moves:
        state=next_state(cur,i,move)
        states.append(state)
    return states

def dfs(cur,end,visited):
    display(cur)

    if(cur==end):
        print("Goal State reached")
        print("\nThe visited states are:")
        for v in visited:
            display(v)
        exit()

    visited.append(cur)
    states=generate_state(cur)

    for state in states:
        if(not state in visited):
            dfs(state,end,visited)
        if count==10:exit()
def main():
    dfs(start,end,visited)
main()