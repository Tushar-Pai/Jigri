"""
vaccum cleaning agent
"""

def clean(floor):
    r = 4
    c = 4
    row, col = 2, 1

    k = 0

    while col != 0:
        print_floor(floor, row, col)
        print('\n')
        col -= 1

    
    while row != 1:
        print_floor(floor, row, col)
        print('')
        if row > 1:
            row -= 1
        else:
            row += 1
    
    
    while k < 12: 
        
        print_floor(floor, row, col)

       
        if floor[row][col] == 1:
            floor[row][col] = 0
            print('The dirt was cleaned')
        else:
            print('No dirt present')
        
    
       
        if row % 2 == 0:
            if 0 < col:
                col -= 1
            else:
                row += 1        
              
        
        else:
            if col < r-1:
                col += 1
            else:
                row += 1 
            
        
        k += 1
        print('\n')
    
        

        
def print_floor(floor, row, col):
    temp = floor[row][col]
    floor[row][col] = '*'
    for i in floor:
        print(i)
    
    floor[row][col] = temp



floor = [[0, 0, 0, 0],
         [0, 0, 0, 1],
         [0, 0, 1, 1],
         [1, 0, 0, 1]]
clean(floor) 
