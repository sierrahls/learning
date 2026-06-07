from typing import Dict # this adds type hinting for Dict

def count_characters(word: str) -> Dict[str, int]:
    count = 0
    dic = {}
    for k in word:
        if k in dic:
            dic[k] += 1
        else:
            dic[k] = 1
    
    return dic




# don't modify below this line
print(count_characters("hello"))
print(count_characters("world"))
print(count_characters("hello world"))
print(count_characters("this is a longer sentence"))
