

"""
Problem:

"""


def count_alphabets(s):
    """
    Args:
     s(str)
    Returns:
     int32
    """
    # Write your code here.
    count = 0
    for char in s:
        if char.isalpha():
            count += 1
    return count


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    s = "#aBdj12C"
    result = count_alphabets(s)

    print(result)