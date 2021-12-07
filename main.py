# This is a sample Python script.

from hello_world import HelloWorld
from chapter_1 import One_One

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    HelloWorld().hello_world()
    print(One_One.IsUnique('Hello World').is_unique())
    print(One_One.IsUnique('Hello').is_unique())
    print(One_One.IsUnique('World').is_unique())
    print(One_One.IsUnique('HelLo').is_unique())


