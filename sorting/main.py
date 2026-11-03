"""Compare Insertion Sort, Merge Sort, Quick Sort and Python sorted()."""
import random
import time
import matplotlib.pyplot as plt


def insertion_sort(a):
    arr = a.copy()
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


def merge_sort(a):
    if len(a) <= 1:
        return a.copy()
    mid = len(a) // 2
    left = merge_sort(a[:mid])
    right = merge_sort(a[mid:])
    merged = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged


def quick_sort(a):
    """Quicksort using a middle element pivot and three-way partitioning."""
    if len(a) <= 1:
        return a.copy()
    pivot = a[len(a) // 2]
    lower = [x for x in a if x < pivot]
    equal = [x for x in a if x == pivot]
    higher = [x for x in a if x > pivot]
    return quick_sort(lower) + equal + quick_sort(higher)


def timed_sort(sort_function, data):
    start = time.perf_counter()
    result = sort_function(data)
    return time.perf_counter() - start, result


def run_benchmark():
    # Insertion Sort is quadratic, so it is capped at 5,000 items to keep
    # the experiment practical. The other algorithms run up to 100,000.
    sizes = [1000, 5000, 10000, 50000, 100000]
    algorithms = {
        "Merge Sort": merge_sort,
        "Quick Sort": quick_sort,
        "Python sorted()": sorted,
    }
    results = {name: [] for name in algorithms}
    results["Insertion Sort"] = []

    print("Input sizes:", sizes)
    for n in sizes:
        data = [random.randint(0, 1_000_000) for _ in range(n)]
        expected = sorted(data)

        for name, function in algorithms.items():
            elapsed, output = timed_sort(function, data)
            assert output == expected
            results[name].append(elapsed)
            print(f"n={n:6} | {name:16} | {elapsed:.6f}s")

        if n <= 5000:
            elapsed, output = timed_sort(insertion_sort, data)
            assert output == expected
            results["Insertion Sort"].append(elapsed)
            print(f"n={n:6} | {'Insertion Sort':16} | {elapsed:.6f}s")
        else:
            results["Insertion Sort"].append(None)

    plt.figure(figsize=(10, 6))
    for name, times in results.items():
        valid = [(n, t) for n, t in zip(sizes, times) if t is not None]
        if valid:
            x, y = zip(*valid)
            plt.plot(x, y, marker="o", label=name)
    plt.xlabel("Input size (n)")
    plt.ylabel("Execution time (seconds)")
    plt.title("Sorting Algorithms Benchmark")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.savefig("sorting_benchmark.png", dpi=150)
    print("\nChart saved as sorting_benchmark.png")
    print("Note: Insertion Sort is limited to n <= 5,000 because of O(n²) growth.")


if __name__ == "__main__":
    run_benchmark()
