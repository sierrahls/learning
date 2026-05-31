from typing import List


def disallow_negatives(num: int) -> int:
    num = max(0, num)
    return num


def max_difference(nums: List[int]) -> int:
    placeholder = 0
    for i in range (1, len(nums)):
        placeholder = max(placeholder, nums[i] - nums[i-1])
    return placeholder

    """
    We set a placeholder value to 0 and start counting at 1, since we already went through 0
    len(nums) is just the last index 
    nums[i] - nums[i-1] lets us compare what is bigger or
    subtract right from left
    [10,1,3,7] -> subtract 1 from 10 = -9
    max(0, -9) its still 0 so our placeholder stays until it gets reassigned
    max(0, 2) -> 2 so placeholder is 2
    max(2,4) -> 4 so placeholder is 4

    so this allows us to find the largest or MAX difference between 2 elements beside eachother

    """


# do not modify below this line
print(disallow_negatives(-2))
print(disallow_negatives(-1))
print(disallow_negatives(0))
print(disallow_negatives(1))
print(disallow_negatives(2))

print(max_difference([1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(max_difference([1, 2, 3, 4, 5, 6, 8, 9]))
print(max_difference([10, 1, 3, 7]))
print(max_difference([2, 4, 7, 5, 7, 8, 4, 2]))
