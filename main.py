# This is a sample Python script.

from hello_world import HelloWorld
from chapter_1 import One_One, One_Two, One_Three

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    HelloWorld().hello_world()
    print('[Question 1.1]')
    print('Hello World has all unique characters:  {}'.format(One_One.IsUnique().is_unique('Hello World')))
    print('Hello has all unique characters:  {}'.format(One_One.IsUnique().is_unique('Hello')))
    print('World has all unique characters:  {}'.format(One_One.IsUnique().is_unique('World')))
    print('HelLo has all unique characters:  {}'.format(One_One.IsUnique().is_unique('HelLo')))
    print()
    print('[Question 1.2]')
    print('abc is a permutation of cba:  {}'.format(One_Two.CheckPermutation().is_permutation('abc', 'cba')))
    print('abc is a permutation of ccc:  {}'.format(One_Two.CheckPermutation().is_permutation('abc', 'ccc')))
    print('hello is a permutation of world:  {}'.format(One_Two.CheckPermutation().is_permutation('hello', 'world')))
    print('hello is a permutation of Hello:  {}'.format(One_Two.CheckPermutation().is_permutation('hello', 'Hello')))
    print('Hello World is a permutation of HWeol rllod:  {}'.format(One_Two.CheckPermutation().is_permutation('Hello World', 'HWeol rllod')))
    print()
    print(One_Three.URLify().urlify('Hello World Hi         ', 14))


