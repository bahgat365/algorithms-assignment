# Maze Solver: BFS vs DFS

## Objective
Find a route through a grid maze and compare Breadth-First Search (BFS) with Depth-First Search (DFS).

## Maze representation
- `#` is a wall.
- `.` is an open cell.
- `S` is the start.
- `E` is the exit.
- `*` marks the resulting path when displayed.

## Algorithms
- BFS uses a queue and finds a shortest path in an unweighted grid.
- DFS uses a stack and finds a path, but does not guarantee the shortest path.
- Parent pointers are used to reconstruct the path after traversal.

## Complexity
For a grid represented as an implicit graph:
- Time: O(V + E).
- Space: O(V).
Here V is the number of open cells and E is the number of valid neighboring connections.

## Run
```bash
python main.py
```
