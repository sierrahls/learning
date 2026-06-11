import heapq
from typing import List


def heap_pop(heap: List[int]) -> List[int]:
    min_heap = []
    for i in range(len(heap)): ##range(len(heap)) helped me solve
        pop = heapq.heappop(heap)
        min_heap.append(pop)

    return min_heap
    

# do not modify below this line
print(heap_pop([1, 2, 3]))
print(heap_pop([1, 3, 2]))
print(heap_pop([6, 7, 8, 12, 9, 10]))
