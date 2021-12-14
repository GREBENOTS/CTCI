from hello_world import HelloWorld
from chapter_1 import One_One, One_Two, One_Three, One_Four, One_Five, One_Six, One_Seven, One_Eight, One_Nine

#  Changed the way that I am doing this main script, since it's getting a bit unwieldy at this point
#  Btw, this main method is not meant to be good code at all---just quick and dirty to actually use the CTCI
#  questions, which ARE meant to be good code themselves.

if __name__ == '__main__':
    HelloWorld().hello_world()
    print('[Question 1.1]')
    one_one = One_One.IsUnique()
    print('Hello World has all unique characters:  {}'.format(one_one.is_unique('Hello World')))
    print('Hello has all unique characters:  {}'.format(one_one.is_unique('Hello')))
    print('World has all unique characters:  {}'.format(one_one.is_unique('World')))
    print('HelLo has all unique characters:  {}'.format(one_one.is_unique('HelLo')))
    print()

    print('[Question 1.2]')
    one_two = One_Two.CheckPermutation()
    print('abc is a permutation of cba:  {}'.format(one_two.is_permutation('abc', 'cba')))
    print('abc is a permutation of ccc:  {}'.format(one_two.is_permutation('abc', 'ccc')))
    print('hello is a permutation of world:  {}'.format(one_two.is_permutation('hello', 'world')))
    print('hello is a permutation of Hello:  {}'.format(one_two.is_permutation('hello', 'Hello')))
    print('Hello World is a permutation of HWeol rllod:  {}'.format(one_two.is_permutation('Hello World', 'HWeol rllod')))
    print()

    print('[Question 1.3]')
    one_three = One_Three.URLify()
    print('One Two Hi, becomes:  {}'.format(one_three.urlify('One Two Hi         ', 10)))
    print('Hello World Yes No Maybe, becomes:  {}'.format(one_three.urlify('Hello World Yes No Maybe               ', 24)))
    print()

    print('[Question 1.4]')
    one_four = One_Four.PalindromePermutation()
    print('tacocat is a permutation of a palindrome:  {}'.format(one_four.is_permutation('tacocat')))
    print('atcocta is a permutation of a palindrome:  {}'.format(one_four.is_permutation('atcocta')))
    print()

    print('[Question 1.5]')
    one_five = One_Five.OneAway()
    print('pale is one edit away from ple:  {}'.format(one_five.is_one_away('pale', 'ple')))
    print('pales is one edit away from pale:  {}'.format(one_five.is_one_away('pales', 'pale')))
    print('pale is one edit away from bale:  {}'.format(one_five.is_one_away('pale', 'bale')))
    print('pale is one edit away from bake:  {}'.format(one_five.is_one_away('pale', 'bake')))
    print('aaaa is one edit away from abaa:  {}'.format(one_five.is_one_away('aaaa', 'abaa')))
    print('aaaa is one edit away from abaaa:  {}'.format(one_five.is_one_away('aaaa', 'abaaa')))
    print()

    print('[Question 1.6]')
    one_six = One_Six.StringCompression()
    print('aabcccccaaa is compressed to:  {}'.format(one_six.compress('aabcccccaaa')))
    print('abc is compressed to:  {}'.format(one_six.compress('abc')))
    print('aaaaaaaaaabbbbbbbbccccccddddeef is compressed to:  {}'.format(one_six.compress('aaaaaaaaaabbbbbbbbccccccddddeef')))
    print()

    print('[Question 1.7]')
    one_seven = One_Seven.RotateMatrix()
    matrix = [
        [0, 2, 4, 6, 8],
        [2, 4, 6, 8, 0],
        [4, 6, 8, 0, 2]
    ]
    print('Rotation Before:  ')
    one_seven.display(matrix)
    print('Rotation After:  ')
    one_seven.rotate(matrix)
    matrix = [
        [0, 2, 4, 6, 8],
        [2, 4, 6, 8, 0],
        [4, 6, 8, 0, 2],
        [6, 8, 0, 2, 4],
        [8, 0, 2, 4, 6]
    ]
    print('Rotation Before:  ')
    one_seven.display(matrix)
    print('Rotation After:  ')
    one_seven.rotate(matrix)
    print()

    print('[Question 1.8]')
    one_eight = One_Eight.ZeroMatrix()
    matrix = [
        [0, 2, 4, 6, 8],
        [2, 4, 6, 8, 9],
        [4, 6, 0, 0, 2],
        [6, 8, 0, 0, 4],
    ]
    print('Matrix Before:  ')
    zero_matrix = One_Eight.ZeroMatrix()
    zero_matrix.display_matrix(matrix)
    zero_matrix.zero_matrix(matrix)
    print('Matrix After:  ')
    zero_matrix.display_matrix(zero_matrix.target_matrix)
    print()

    matrix = [
        [1, 2, 4, 6, 8],
        [2, 4, 6, 8, 9],
        [4, 6, 0, 0, 2],
        [6, 8, 2, 4, 4],
    ]
    print('Matrix Before:  ')
    zero_matrix = One_Eight.ZeroMatrix()
    zero_matrix.display_matrix(matrix)
    zero_matrix.zero_matrix(matrix)
    print('Matrix After:  ')
    zero_matrix.display_matrix(zero_matrix.target_matrix)
    print()
    print('End chapter 1')