

"""
Problem:
Reverse Words In A Given String
Given a string s, your task is to reverse the words of s.

Example One
{
"s": "best technical interview prep courses",
}
Output:

courses prep interview technical best
Example Two
{
"s": "kickstart",
}
Output:

kickstart
Notes
Constraints:

length of s <= 105
"""


def reverse_words(s):
    """
    Args:
     numbers(list_int32)
    Returns:
     int32
    """
    # Write your code here.
    result = []
    end = len(s)
    for i in range(len(s) - 1, -1, -1):
        print(i)
        if s[i] == ' ' or i == 0:
            if i == 0:
                word = s[0: end]
            else:
                word = s[i + 1: end]
            result.append(word)
            end = i

    return result


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    s = "best technical interview prep courses" # 12

    result = reverse_words(s)

    print(result)