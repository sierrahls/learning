from typing import List


def find_max_in_each_list(nested_arr: List[List[int]]) -> List[int]:
    placeholder = []
    for subarr in nested_arr:
        largest = subarr[0] #this is the first element as the "best guess"
        for element in subarr:
            if element >= largest:
                largest = element
        placeholder.append(largest)

    return placeholder

    


# do not modify below this line
print(find_max_in_each_list([[1, 2], [3, 4, 2]]))
print(find_max_in_each_list([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print(find_max_in_each_list([[5, 6, 2, 8], [9], [9, 10], [11, 10, 11]]))