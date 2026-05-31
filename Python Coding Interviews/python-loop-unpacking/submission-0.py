from typing import List, Tuple


def best_student(scores: List[Tuple[str, int]]) -> str:
    placeholder = -1
    best_name = ""
    for x, y in scores:
        if y > placeholder:
            placeholder = y
            best_name = x
    
    return best_name


# do not modify below this line
print(best_student([("Alice", 90), ("Bob", 80), ("Charlie", 70)]))
print(best_student([("Alice", 90), ("Bob", 80), ("Charlie", 100)]))
print(best_student([("Alice", 90), ("Bob", 100), ("Charlie", 70)]))
print(best_student([("Alice", 90), ("Bob", 90), ("Charlie", 80), ("David", 100)]))