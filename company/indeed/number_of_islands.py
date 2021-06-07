



#https://leetcode.com/discuss/interview-question/1063081/Indeed-or-Karat-(Video-Screen)-or-Find-Rectangless

#Question 1
#Given a 2D array of 0s and 1s, return the position of the single rectangle made up of 1s.

# Example input
grid = [ [0, 0, 0, 0, 0],
         [0, 1, 1, 1, 0],
         [0, 1, 1, 1, 0],
         [0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0] ]
# you should return the
# (start_row, start_col, end_row, end_col)
 #        [ 1, 1, 2, 3 ]

#Question 2
#Multiple rectangles. Given a 2D array of 0s and 1s, return a list of the postions of all rectangles made up of 1s. Note: you are not allowed to change the input matrix.

# Example 1 input
grid1 =[ [0, 0, 0, 0, 0, 0, 1],
         [0, 0, 0, 0, 0, 0, 0],
         [1, 0, 0, 1, 1, 1, 0],
         [0, 1, 0, 1, 1, 1, 0],
         [0, 1, 0, 0, 0, 0, 0],
         [0, 1, 0, 1, 1, 0, 0],
         [0, 0, 0, 1, 1, 0, 0],
         [1, 0, 0, 0, 0, 0, 0] ]

# return list of (start_row, start_col, end_row, end_col)
# for each rectangle:
grid_= [ (0, 6, 0, 6),
   (2, 0, 2, 0),
   (2, 3, 3, 5),
   (3, 1, 5, 1),
   (5, 3, 6, 4),
   (7, 0, 7, 0) ]
#More examples

grid2 = [ [1] ]
# you should return [ (0,0,0,0) ]

grid3 = [ [0, 0, 0, 0, 0],
          [0, 1, 1, 1, 0],
          [0, 1, 1, 1, 0],
          [0, 1, 1, 1, 0],
          [0, 0, 0, 0, 0] ]
# you should return [ (1, 1, 3, 3) ]


grid4 = [
  [1,1,0,0,0],
  [1,1,0,0,0],
  [0,0,1,0,0],
  [0,0,0,1,1]
]
# This is similar to problem https://leetcode.com/problems/number-of-islands/

#Problem #1

def solve1(grid):
    found = False
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                s_row, s_col = i, j
                e_row, e_col = i+1,j+1
                while e_row < len(grid) and grid[e_row][j]:
                    e_row += 1
                while e_col < len(grid[0]) and grid[i][e_col]:
                    e_col += 1
                e_row -= 1
                e_col -= 1
                found = True
                break
        if found:
            break

    return [s_row, s_col, e_row, e_col]
#Problem 2


def solve2(grid):
    output = []
    visited = set()
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if (i,j) in visited:
                continue
            visited.add((i,j))
            if grid[i][j] == 1:
                s_row, s_col = i, j
                e_row, e_col = i+1,j+1
                while e_row < len(grid) and grid[e_row][j]:
                    e_row += 1
                while e_col < len(grid[0]) and grid[i][e_col]:
                    e_col += 1
                for x in range(s_row, e_row):
                    for y in range(s_col, e_col):
                        visited.add((x,y))
                e_row -= 1
                e_col -= 1
                output.append([s_row, s_col, e_row, e_col])
    return output


print(solve1(grid))