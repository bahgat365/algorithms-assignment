"""Priority-based Task Scheduler implemented with a custom Max Heap."""
from dataclasses import dataclass
import random


@dataclass
class Task:
    name: str
    priority: int
    arrival_time: int

    def __str__(self):
        return (f"{self.name} (priority={self.priority}, "
                f"arrival={self.arrival_time})")


class MaxHeap:
    def __init__(self):
        self.heap = []

    def __len__(self):
        return len(self.heap)

    def insert(self, task):
        self.heap.append(task)
        self._sift_up(len(self.heap) - 1)

    def extract_max(self):
        if not self.heap:
            raise IndexError("Cannot extract from an empty heap.")
        if len(self.heap) == 1:
            return self.heap.pop()

        maximum = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._sift_down(0)
        return maximum

    def _sift_up(self, index):
        while index > 0:
            parent = (index - 1) // 2
            if self.heap[parent].priority >= self.heap[index].priority:
                break
            self.heap[parent], self.heap[index] = self.heap[index], self.heap[parent]
            index = parent

    def _sift_down(self, index):
        size = len(self.heap)
        while True:
            largest = index
            left = 2 * index + 1
            right = 2 * index + 2

            if left < size and self.heap[left].priority > self.heap[largest].priority:
                largest = left
            if right < size and self.heap[right].priority > self.heap[largest].priority:
                largest = right
            if largest == index:
                break

            self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
            index = largest


def main():
    scheduler = MaxHeap()
    tasks = [
        Task("Task A", 3, 1),
        Task("Task B", 9, 2),
        Task("Task C", 5, 3),
        Task("Task D", 7, 4),
    ]

    print("Adding tasks to the scheduler:")
    for task in tasks:
        scheduler.insert(task)
        print("  INSERT:", task)

    print("\nExecution order (highest priority first):")
    while len(scheduler):
        print("  EXTRACT-MAX:", scheduler.extract_max())

    print("\nRandom task experiment:")
    random_scheduler = MaxHeap()
    for number in range(1, 21):
        random_scheduler.insert(
            Task(f"Job {number}", random.randint(1, 10), number)
        )

    while len(random_scheduler):
        print(" ", random_scheduler.extract_max())


if __name__ == "__main__":
    main()
