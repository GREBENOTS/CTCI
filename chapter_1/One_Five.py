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
