

"""
Problem:

First Occurrence Of A Character
Find the first occurrence of a given character in a given string.

Example One
{
"s": "interview",
"to_find": "e"
}
Output:

3
Example Two
{
"s": "kickstart",
"to_find": "n"
}
Output:

-1
Notes
Return -1 if the character is not present.

Constraints:

0 <= length of string <= 104.
Given string contains lower case English alphabets only.
The given character can be any lower case English alphabet.
"""


def find_first_occurrence(s, to_find):
    """
    Args:
     s(str)
     to_find(char)
    Returns:
     int32
    """
    # Write your code here.
    for i in range(0, len(s)):
        if s[i] == to_find:
            return i
    return -1


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    s = "interview"
    to_find = 'e'
    result = find_first_occurrence(s, to_find)

    print(result)