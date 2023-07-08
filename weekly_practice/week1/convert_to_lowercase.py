

"""
Problem:

"""


def uppercase_to_lowercase(s):
    """
    Args:
     s(str)
    Returns:
     str
    """
    # Write your code here.
    lowercase = ""
    for char in s:
        if char.isupper():
            lowercase += char.lower()
        else:
            lowercase += char
    return lowercase


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    s = "InTerView"

    result = uppercase_to_lowercase(s)

    print(result)