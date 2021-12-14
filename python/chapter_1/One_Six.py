"""
String Compression:  Implement a method to perform basic string compression using the counts of repeated characters.
For example, the string aabcccccaaa would become a2b1c5a3.  If the compressed string would not become smaller than the
original string, your method should return the original string.  You can assume the string has only uppercase and
lowercase letters (a-z).
"""


class StringCompression:
    def __init__(self):
        self.target_string = ''

    def compress(self, s):
        char_array = list(s)

        current = char_array[0]
        last = current
        repeat_count = 0
        for c in char_array:
            if c == current:
                repeat_count += 1
                last = current
                current = c
                continue
            else:
                added_string = ''.join([last, str(repeat_count)])
                self.target_string = ''.join([self.target_string, added_string])
                repeat_count = 1
                last = c
                current = c
        else:  # If there isn't a break, do this last.  (I think this is a bad pattern, but it works I guess)
            added_string = ''.join([last, str(repeat_count)])
            self.target_string = ''.join([self.target_string, added_string])

        return self.target_string if len(self.target_string) < len(s) else s
