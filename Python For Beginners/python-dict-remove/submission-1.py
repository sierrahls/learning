from typing import Dict, List

def remove_keys(my_dict: Dict[str, int], keys: List[str]) -> Dict[str, int]:
    for i in keys:  #iterate through keys elements
        if i in my_dict: #if the element in keys is in my_dict
            my_dict.pop(i) #we pop it
            #otherwise its ignored

    return my_dict




# do not modify below this line
print(remove_keys({"a": 1, "b": 2, "c": 3}, ["a", "c"]))
print(remove_keys({"a": 1, "b": 2, "c": 3}, ["d"]))
