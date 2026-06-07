from typing import Dict # this adds type hinting for Dict

def count_characters(word: str) -> Dict[str, int]:
    dic = {}
    for k in word: #each char in str
        if k in dic: #if char is in the str
            dic[k] += 1 #we increment its count
        else:
            dic[k] = 1 #we assign it to our dic with a count of 1
    
    return dic




# don't modify below this line
print(count_characters("hello"))
print(count_characters("world"))
print(count_characters("hello world"))
print(count_characters("this is a longer sentence"))
