# Sorting Benchmark Lab

## Objective
Compare Insertion Sort, Merge Sort, Quick Sort, and Python's built-in `sorted()`.

## Method
- Generate random integer arrays.
- Test input sizes 1,000, 5,000, 10,000, 50,000, and 100,000.
- Measure execution time using `time.perf_counter()`.
- Verify each output against Python's `sorted()` result.
- Plot the measured running times.

## Complexity
- Insertion Sort: average/worst O(n²).
- Merge Sort: O(n log n).
- Quick Sort: average O(n log n), worst O(n²).
- Python `sorted()`: Timsort, O(n log n) worst case.

## Important experimental note
Insertion Sort is measured only up to 5,000 elements because its quadratic growth makes larger tests unnecessarily slow. The other algorithms are tested up to 100,000.

## Requirements and Run
```bash
pip install matplotlib
python main.py
```
The chart is saved as `sorting_benchmark.png`.
