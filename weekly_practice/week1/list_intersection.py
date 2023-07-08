# Falied too slow O(n*m)
"""

"""


def get_intersection_with_maintained_frequency(a, b):
    """
    Args:
     a(list_int32)
     b(list_int32)
    Returns:
     list_int32
    """
    # Write your code here.

    result = []
    count1 = 0
    while count1 < len(a):
        for count2 in range(len(b)):
            if a[count1] == b[count2]:
                result.append(b[count2])
                b[count2] = 'f'
                break
        count1 += 1

    return result


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    # a = [7, 7, 14, 92, 14, 92, 92]
    # b = [0, 0, 92, 92, 7]
    # a = [1]
    # b = [1]
    # a = [4, 2, 2, 3, 1]
    # b = [2, 2, 2, 3, 3]
    # a = []
    # b = []
    # a = [-1000000, 0, 0, 1, 1, -1000000, 7]
    # b = [-1000000, 0, 0, 1, 1, -1000000, 7]
    # a = [1000000, 1000000, 0, 1, -13, 5, 0]
    # b = [0, 5, -13, 1, 0, 1000000, 1000000]
    a = [2, 2, 1, 3, 2]
    b = [1, 100, 2, 2, 20, 99, 100]

    result = get_intersection_with_maintained_frequency(a, b)

    print(result)




# for item1 in freq_a.keys():
#     for item2 in freq_b.keys():
#         if item1 == item2:
#             multiplier = min(freq_a[item1], freq_b[item2])
#             for element in range(0, multiplier):
#                 result.append(item1)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
