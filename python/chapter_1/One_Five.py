"""
One Away:  There are three types of edits that can be performed on strings:  insert a character, remove a character,
or replace a character.  Given two strings, write a function to check if they are one edit (or zero edits) away.

Example:
    pale, ple --> True
    pales, pale --> True
    pale, bale --> True
    pale, bake --> False
"""


class OneAway:
    def __init__(self):
        self.target_string = ''

    def is_one_away(self, starting_string, target_string):
        self.target_string = target_string

        char_array_start = list(starting_string)
        char_array_target = list(self.target_string)

        #  Logic for different lengths is simpler, so lets do that first
        num_changes = 0
        if True:  # Only an insert will be allowed
            for i in range(0, len(char_array_start)):
                if i < len(char_array_target):
                    if char_array_start[i] == char_array_target[i]:
                        continue
                if len(char_array_start) != len(char_array_target):
                    char_array_target.insert(i, char_array_start[i])
                else:
                    char_array_target[i] = char_array_start[i]
                num_changes += 1

            if num_changes != 1:
                return False
            return True
