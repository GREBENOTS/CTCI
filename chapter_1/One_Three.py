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
        self.target_string = list(s)
        s_length = len(self.target_string)

        #  First, find the number of spaces
        num_spaces = 0
        buffer_found = False
        for i in range(s_length - 1, -1, -1):
            if not buffer_found:
                if self.target_string[i] == ' ':
                    continue
                else:
                    buffer_found = True
            if self.target_string[i] == ' ':
                num_spaces += 1

        move_amount = num_spaces * 2  # '%20' is 2 extra characters, vs ' '

        #  Now, we actually do the substituting
        buffer_found = False
        for i in range(s_length - 1, -1, -1):
            if not buffer_found:
                if self.target_string[i] == ' ':
                    continue
                else:
                    buffer_found = True
            if self.target_string[i] != ' ':
                self.target_string[i + move_amount] = self.target_string[i]
            else:
                self.target_string[i] = '%'
                self.target_string[i+1] = '2'
                self.target_string[i+2] = '0'
                move_amount -= 2

        return self.target_string
