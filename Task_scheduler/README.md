# Task Scheduler Using a Max Heap

## Objective
Simulate a scheduler that always executes the most urgent task first.

## Features
- A `Task` has a name, priority, and arrival time.
- A custom array-based Max Heap is implemented.
- `INSERT` adds a task.
- `EXTRACT-MAX` removes the task with the highest priority.
- Includes a fixed example and 20 randomly generated tasks.

## Heap operations
- INSERT: O(log n)
- EXTRACT-MAX: O(log n)
- Maximum priority lookup: O(1)

## Run
```bash
python main.py
```

The implementation uses a custom Max Heap rather than Python's built-in priority queue, to demonstrate the lecture's heap operations.
