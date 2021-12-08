"""
URLify:  Write a method to replace all spaces in a string with '%20'.  You may assume that the string has sufficient
space at the end to hold the additional characters, and that you are given the true length of the string.
Input:  'Mr John Smith    ', 13
Output:  'Mr%20John%20Smith
"""


class URLify:
    def __init__(self):
        self.target_string = ''

    def urlify(self, s, length):
        char_list = list(s)
        s_length = len(char_list)

        #  First, find the number of spaces
        num_spaces = 0
        buffer_found = False
        for i in range(s_length - 1, -1, -1):
            if not buffer_found:
                if char_list[i] == ' ':
                    continue
                else:
                    buffer_found = True
            if char_list[i] == ' ':
                num_spaces += 1

        #  Now, we actually do the substituting
        num_left = num_spaces
        buffer_found = False
        for i in range(s_length - 1, -1, -1):
            if not buffer_found:
                if char_list[i] == ' ':
                    continue
                else:
                    buffer_found = True
            if char_list[i] != ' ':
                char_list[i + (2 * num_left)] = char_list[i]
            else:
                char_list[i + (2 * num_left)] = '0'
                char_list[i + (2 * num_left) - 1] = '2'
                char_list[i + (2 * num_left) - 2] = '%'
                num_left -= 1

        return self.target_string.join(char_list)
