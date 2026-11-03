"""Solve a grid maze using BFS and DFS, then compare the traversals."""
from collections import deque

MAZE = [
    list("S..#...."),
    list("##......"),
    list("...#...#"),
    list(".###.#.."),
    list(".......E"),
]

START = (0, 0)
END = (4, 7)
DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def get_neighbors(position):
    row, col = position
    neighbors = []
    for dr, dc in DIRECTIONS:
        nr, nc = row + dr, col + dc
        if 0 <= nr < len(MAZE) and 0 <= nc < len(MAZE[0]):
            if MAZE[nr][nc] != "#":
                neighbors.append((nr, nc))
    return neighbors


def reconstruct_path(parent, end):
    if end not in parent:
        return []
    path = []
    current = end
    while current is not None:
        path.append(current)
        current = parent[current]
    return list(reversed(path))


def bfs():
    queue = deque([START])
    parent = {START: None}
    visited_order = []

    while queue:
        current = queue.popleft()
        visited_order.append(current)
        if current == END:
            break

        for neighbor in get_neighbors(current):
            if neighbor not in parent:
                parent[neighbor] = current
                queue.append(neighbor)

    return reconstruct_path(parent, END), visited_order


def dfs():
    stack = [START]
    parent = {START: None}
    visited_order = []

    while stack:
        current = stack.pop()
        visited_order.append(current)
        if current == END:
            break

        # Reverse to make the exploration order easier to follow.
        for neighbor in reversed(get_neighbors(current)):
            if neighbor not in parent:
                parent[neighbor] = current
                stack.append(neighbor)

    return reconstruct_path(parent, END), visited_order


def display_maze(path):
    drawing = [row.copy() for row in MAZE]
    for row, col in path:
        if drawing[row][col] not in ("S", "E"):
            drawing[row][col] = "*"
    for row in drawing:
        print("".join(row))


def main():
    print("Original maze:")
    for row in MAZE:
        print("".join(row))

    bfs_path, bfs_visited = bfs()
    dfs_path, dfs_visited = dfs()

    print("\nBFS result:")
    print("Path:", bfs_path)
    print("Path length (moves):", len(bfs_path) - 1 if bfs_path else "No path")
    print("Visited cells:", len(bfs_visited))
    display_maze(bfs_path)

    print("\nDFS result:")
    print("Path:", dfs_path)
    print("Path length (moves):", len(dfs_path) - 1 if dfs_path else "No path")
    print("Visited cells:", len(dfs_visited))
    display_maze(dfs_path)

    print("\nComparison:")
    print("BFS finds a shortest path in an unweighted grid.")
    print("DFS finds a path, but it is not guaranteed to be shortest.")


if __name__ == "__main__":
    main()
