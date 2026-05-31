from typing import List


def get_index_of_seven(nums: List[int]) -> int:
    for x,y in enumerate(nums):
        if y == 7:
            return x
    return -1


def get_dist_between_sevens(nums: List[int]) -> int:
    placeholder = -1
    for x, y in enumerate(nums):
        if y == 7:
            if placeholder == -1:
                placeholder = x
            else:
                return x - placeholder
            


# do not modify below this line
print(get_index_of_seven([1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(get_index_of_seven([1, 2, 3, 4, 5, 6, 8, 9]))
print(get_index_of_seven([2, 4, 7, 5, 7, 8, 4, 2]))

print(get_dist_between_sevens([1, 2, 7, 4, 5, 6, 7, 8, 9]))
print(get_dist_between_sevens([2, 7, 7, 7, 8]))
print(get_dist_between_sevens([7, 4, 8, 4, 2, 7]))
