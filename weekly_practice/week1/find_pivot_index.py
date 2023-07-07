"""
Problem

Find Pivot Index Given alist
of
integers
numbers, calculate
the
pivot
index
of
this
list.

The
pivot
index is the
index
where
the
sum
of
all
the
numbers
strictly
to
the
left
of
the
index is equal
to
the
sum
of
all
the
numbers
strictly
to
the
index
's right. If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left. This also applies to the right edge of the array.

Return
the
leftmost
pivot
index.If
no
such
index
exists,
return -1.

Example
One
{
    "numbers": [2, 3, 1, -1, 1, 1, 4]
}
Output:

2
Considering
index
2 as pivot
index, left
subarray = [2, 3] and right
subarray = [-1, 1, 1, 4].Here, sum(left
subarray) = sum(right
subarray) = 5.

Here, index
4 is also
a
valid
pivot
index.But
index
2 is leftmost.

Example
Two
{
    "numbers": [2, 3, 5]
}
Output:

-1
Example
Three
{
    "numbers": [0, 1, -1]
}
Output:

0
Notes
Constraints:

1 <= size
of
the
input
list <= 104
-105 <= any
element
of
the
input
list <= 105

{
"numbers": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 0, -55, 0, 0]
}
ans: 12

{
"numbers": [1, 2, 3, 4, 5, -15, 7]
}

ans 6

{
"numbers": [2, 3, 1, -1, 1, 1, 4]
}

2

{
"numbers": [1, 2, -3, 1, 2, 3, -6, 1, 2, 3, 4, -10, 0, -100000, 100000]
}

12

"""


def get_pivot_index(numbers):
    """
    Args:
     numbers(list_int32)
    Returns:
     int32
    """
    # Write your code here.
    left_sum = 0
    right_sum = sum(numbers) - numbers[0]
    if left_sum == right_sum:
        return 0
    for number in range(1, len(numbers)):
        left_sum += numbers[number - 1]
        right_sum -= numbers[number]
        if left_sum == right_sum:
            return number
    return -1


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    numbers = [1, 2, -3, 1, 2, 3, -6, 1, 2, 3, 4, -10, 0, -100000, 100000] # 12
    # numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 0, -55, 0, 0] # 12
    # numbers = [2, 3, 1, -1, 1, 1, 4] # 2
    # numbers = [1, 2, 3, 4, 5, -15, 7] # 6
    # numbers = [2, 3, 1, -1, 1, 1, 4]
    # numbers = [2, 3, 5]
    # numbers = [0, 1, -1]
    # numbers = [2, 3, 1,  1, 1, 4, -11]
    result = get_pivot_index(numbers)

    print(result)





