
def clean(floor):
 row = len(floor)
 col = len(floor[0])
 for i in range(0, row):
  if(i%2 == 0):
   for j in range(0, col):
    if(floor[i][j] == 1):
      print("Status : Dirty")
      print_floor(floor, i, j)
      floor[i][j] = 0
      print("Cleaned")
      print_floor(floor, i, j)
    else:
     print("Status : Clean")
     print_floor(floor, i, j)
  else:
   for j in range(col-1, -1, -1):
    if(floor[i][j] == 1):
      print("status : Dirty")
      print_floor(floor, i, j)
      floor[i][j] = 0
      print("Cleaned")
      print_floor(floor, i, j)
    else:
      print("Status : Clean")
      print_floor(floor, i, j)

 print("Status : all states Cleaned")

def print_floor(floor, row, col):
  for i in range(0, len(floor)):
    for j in range(0, len(floor[0])):
      if(i == row and j == col):
        print(f"|{floor[i][j]}|", end=" ")
      else:
        print(f" {floor[i][j]} ", end=" ")
    print(end='\n')
  print(end='\n')


print("Enter no. of rows")
m = int(input())
print("Enter no.of columns")
n = int(input())
print("Enter the tile status")
floor = []
for i in range(0, m):
  a = list(map(int, input().split(" ")))
  floor.append(a)
print()
clean(floor)


   
