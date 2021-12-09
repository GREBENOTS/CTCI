# This is a sample Python script.

from hello_world import HelloWorld
from chapter_1 import One_One, One_Two, One_Three, One_Four, One_Five

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
    print('[Question 1.3]')
    print('One Two Hi, becomes:  {}'.format(One_Three.URLify().urlify('One Two Hi         ', 10)))
    print('Hello World Yes No Maybe, becomes:  {}'.format(One_Three.URLify().urlify('Hello World Yes No Maybe               ', 24)))
    print()
    print('[Question 1.4]')
    print('tacocat is a permutation of a palindrome:  {}'.format(One_Four.PalindromePermutation().is_permutation('tacocat')))
    print('atcocta is a permutation of a palindrome:  {}'.format(One_Four.PalindromePermutation().is_permutation('atcocta')))
    print()
    print('[Question 1.5]')
    print('pale is one edit away from ple:  {}'.format(One_Five.OneAway().is_one_away('pale', 'ple')))
    print('pales is one edit away from pale:  {}'.format(One_Five.OneAway().is_one_away('pales', 'pale')))
    print('pale is one edit away from bale:  {}'.format(One_Five.OneAway().is_one_away('pale', 'bale')))
    print('pale is one edit away from bake:  {}'.format(One_Five.OneAway().is_one_away('pale', 'bake')))
    print('aaaa is one edit away from abaa:  {}'.format(One_Five.OneAway().is_one_away('aaaa', 'abaa')))
    print('aaaa is one edit away from abaaa:  {}'.format(One_Five.OneAway().is_one_away('aaaa', 'abaaa')))

