import os

print(os.path.dirname(os.path.dirname(__file__)))
print(os.path.split(os.path.abspath(__file__)))
print(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
print(os.path.dirname(os.path.realpath(__file__)).rsplit(os.sep, 2))