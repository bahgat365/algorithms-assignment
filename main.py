"""Empirical analysis of Insertion Sort."""
import random
import time
import matplotlib.pyplot as plt


def insertion_sort(values):
    """Sort values and return (sorted_values, comparisons, shifts)."""
    arr = values.copy()
    comparisons = 0
    shifts = 0

    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0:
            comparisons += 1
            if arr[j] > key:
                arr[j + 1] = arr[j]
                shifts += 1
                j -= 1
            else:
                break

        arr[j + 1] = key

    return arr, comparisons, shifts


def make_data(size, case):
    if case == "sorted":
        return list(range(size))
    if case == "reverse":
        return list(range(size, 0, -1))
    data = list(range(size))
    random.shuffle(data)
    return data


def run_experiment():
    sizes = [100, 500, 1000, 2000, 3000, 5000]
    cases = ["sorted", "reverse", "random"]
    results = {case: {"time": [], "comparisons": [], "shifts": []} for case in cases}

    for case in cases:
        for size in sizes:
            data = make_data(size, case)
            start = time.perf_counter()
            sorted_data, comparisons, shifts = insertion_sort(data)
            elapsed = time.perf_counter() - start

            assert sorted_data == sorted(data)
            results[case]["time"].append(elapsed)
            results[case]["comparisons"].append(comparisons)
            results[case]["shifts"].append(shifts)
            print(f"{case:7} | n={size:5} | time={elapsed:.6f}s "
                  f"| comparisons={comparisons:10} | shifts={shifts:10}")

    plt.figure(figsize=(9, 5))
    for case in cases:
        plt.plot(sizes, results[case]["time"], marker="o", label=case.title())
    plt.xlabel("Input size (n)")
    plt.ylabel("Execution time (seconds)")
    plt.title("Insertion Sort: Experimental Running Time")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.savefig("insertion_sort_runtime.png", dpi=150)
    print("\nChart saved as insertion_sort_runtime.png")

    return sizes, results


if __name__ == "__main__":
    run_experiment()
