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


"""


def get_pivot_index(numbers):
    """
    Args:
     numbers(list_int32)
    Returns:
     int32
    """
    # Write your code here.

    return 0


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    numbers = [2, 3, 1, -1, 1, 1, 4]
    result = get_pivot_index(numbers)

    print(result)




# for item1 in freq_a.keys():
#     for item2 in freq_b.keys():
#         if item1 == item2:
#             multiplier = min(freq_a[item1], freq_b[item2])
#             for element in range(0, multiplier):
#                 result.append(item1)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
