#Program to implement algorithm of n-Queens problem containing n cube cells
import math
def is_safe_move(mat,row,col):
  for i in range(row):
    if mat[i][col]=='Q':
      return False

  (i,j)=(row,col)
  while i >= 0 and j >= 0:
    if mat[i][j]=='Q':
      return False
    i = i-1
    j = j-1

  (i,j)=(row,col)
  while i >= 0 and j < N:
    if mat[i][j]=='Q':
      return False
    i = i-1
    j = j+1

  return True

def n_Queen(mat,r):
  #base condition for recursive routine
  #if queens placed successfully
  if r == N:
    ''' 
    For visualization , we collapse to one of the possible solutions by adding an equivalence between the rows and z-axis'''

    print("")
    print("==="*6)
    print("possible solution")
    print("==="*6)
    for z in range(N):
      print("Z coordinate:"+str(z))
      print("  0 1 2 3 4 5 6 7")
      #gives 2D matrix
      for x in range(N):
        for y in range(N):
          #idea is to spread each queen into different x,y,z
          if z != x:
            #just for printing index to help identify coordinate index (x,y,z)
            if y == 0:
              print("{} {}".format(x, "-"), end=" ")
            else:
              print("-", end=" ")
          else:
            #just for printing index to help identify coordinate index (x,y,z)
            if y == 0:
              print("{} {}".format(x, mat[x][y]), end=" ")
            else:
              print(mat[x][y], end=" ")

        print()

    global counter
    counter = counter+1
    return 

  for i in range(N):
    if is_safe_move(mat,r,i):
      mat[r][i] = 'Q'
      n_Queen(mat,r+1)
      mat[r][i] = '-'

