start=[1,2,3,-1,4,5,6,7,8]
end=[1,2,3,4,5,-1,6,7,8]
visited=[]
count=0
def display(state):
    for i in range(9):
        if(i%3==0):print('')
        print(state[i],end="  ")
    print("\n---------")


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

def dfs(cur,end,visited,limit,count):

    display(cur)
    
    if(cur==end):
        print("Goal reached!")
        exit()
    if(count==limit):
        return
    visited.append(cur)
    states=generate_state(cur)
    for state in states:
        if(not state in visited):
            dfs(state,end,visited,limit,count+1)
        if count==10:exit()

def iddfs(start,end,visited,max_limit):
    cur=start[:]
    count=0
    if(cur==end):print("goal reached!")
    visited.append(cur)
    for i in range(1,max_limit+1):
        l=len(visited)
        cur=dfs(visited[l-1],end,visited,i,0)
        count=count+1
    if(count==max_limit):
        print("Could not reach in limit")
    
def main():
    iddfs(start,end,visited,10)
main()



# start=[]
# end=[]
# print("Enter start state:")
# for i in range(9):
#     t=int(input())
#     start.append(t)
# print("Enter end state:")
# for i in range(9):
#     t=int(input())
#     end.append(t)