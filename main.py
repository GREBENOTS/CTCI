# This is a sample Python script.

from hello_world import HelloWorld
from chapter_1 import One_One, One_Two

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    HelloWorld().hello_world()
    print('Question 1.1')
    print(One_One.IsUnique().is_unique('Hello World'))
    print(One_One.IsUnique().is_unique('Hello'))
    print(One_One.IsUnique().is_unique('World'))
    print(One_One.IsUnique().is_unique('HelLo'))
    print('\n')

    print('Question 1.2')
    print(One_Two.CheckPermutation().is_permutation('asbsc', 'cbass'))


