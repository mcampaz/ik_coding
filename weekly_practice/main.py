# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


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
    freq_a = {}
    freq_b = {}
    freq_r = {}
    for count1 in range(0, len(a)):
        if a[count1] in freq_a.keys():
            freq_a[a[count1]] += 1
        else:
            freq_a[a[count1]] = 1

    for count2 in range(0, len(b)):
        if b[count2] in freq_b.keys():
            freq_b[b[count2]] += 1
        else:
            freq_b[b[count2]] = 1
    for item1 in freq_a.keys():
        for item2 in freq_b.keys():
            if item1 == item2:
                multiplier = min(freq_a[item1], freq_b[item2])
                for element in range(0, multiplier):
                    result.append(item1)

    return result, freq_a, freq_b, freq_r


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    a = [7, 7, 14, 92, 14, 92, 92]
    b = [0, 0, 92, 92, 7]
    # a = [1]
    # b = [1]
    result, freq_a, freq_b, freq_r = get_intersection_with_maintained_frequency(a, b)

    print(result)
    print(freq_a.keys())
    print(freq_a.values())
    print(freq_b.keys())
    print(freq_b.values())
    print(freq_r.keys())
    print(freq_r.values())
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
