

"""
Problem:

TO DO: REFACTORING TO ONE FUNCTION

Length Of The Last Word
Find the length of the last word in a given sentence.

Example One
{
"sentence": "Interview Kickstart"
}
Output:

9
Example Two
{
"sentence": " Hello World  "
}
Output:

5
Notes
A word is defined as a character sequence consisting of non-space characters only.
If the last word doesn't exist, output 0.
Constraints:

0 <= length of input sentence <= 105
Given sentence contains lowercase and uppercase English alphabets and space characters ' '.

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
    last_char = len(s)
    while s[last_char - 1].isspace() and last_char >= 0:
        last_char -= 1
    if last_char <= 0:
        return result
    for i in range(last_char - 1, -1, -1):
        if s[i] == ' ' or i == 0:
            if i == 0:
                word = s[0: last_char]
            else:
                word = s[i + 1: last_char]
            result.append(word)
            return result

    return result


def length_of_last_word(sentence):
    """
    Args:
     sentence(str)
    Returns:
     int32
    """
    # Write your code here.
    if len(sentence) == 0:
        return 0
    length_last_word = 0
    last_word = reverse_words(sentence)  # list with last word
    if len(last_word) == 0:
        return 0
    for char in last_word[0]:
        length_last_word += 1
    return length_last_word


def length_of_last_word(sentence):
    """
    Args:
     sentence(str)
    Returns:
     int32
    """
    # Write your code here.
    length_last_word = 0
    last_word = reverse_words(sentence)  # list with last word
    if len(last_word) == 0:
        return 0
    for char in last_word[0]:
        length_last_word += 1
    return length_last_word


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    sentence = "Interview Kickstart   "

    result = length_of_last_word(sentence)

    print(result)
