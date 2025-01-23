# Robot Navigator

You have a robot on a grid that starts at position $(0,0)$. The robot follows a sequence of instructions to move around the grid. The grid has an infinite size in all directions.

The possible instructions are:

 - `UP x` - Move x units up
 - `DOWN x` - Move x units down 
 - `LEFT x` - Move x units left
 - `RIGHT x` - Move x units right

Your task is to determine the final position of the robot after it executes all the instructions.

# Input

The first line contains the number of instructions. The next lines contain 1 instruction per line. The instructions have the direction and the number of units for that direction.

# Output

The output contains one line with the final coordinates of the robot in the format: (x,y)

# Sample Input
```
5
UP 3
RIGHT 4
DOWN 2
LEFT 1
UP 1
```
# Output
```
3 2
```
\newpage
