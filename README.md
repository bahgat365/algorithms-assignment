# Insertion Sort Analysis

## Objective
Empirically analyze Insertion Sort on sorted, reverse-sorted, and random inputs.

## Features
- Implements Insertion Sort.
- Counts key comparisons and element shifts.
- Measures execution time with `time.perf_counter()`.
- Plots running time for different input sizes.

## Complexity
- Best case: O(n) time (already sorted input).
- Average case: O(n²) time.
- Worst case: O(n²) time (reverse-sorted input).
- Auxiliary space: O(1).

## Requirements
Python 3. Install Matplotlib with `pip install matplotlib`.

## Run
```bash
python main.py
```

The program prints measurements and saves `insertion_sort_runtime.png`.
