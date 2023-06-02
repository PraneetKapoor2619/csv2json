import os
import sys
import time

import json

import pickle

class Foo:
    def __init__(self):
        self.x = 10
        self.y = 12
        self.matrix = [[1, 2, 3],
                        [5, 6, 7],
                        [8, 9, 10]]
    def mul(self):
        self.x = self.x * self.y

obj1 = Foo()
obj1_json = json.dumps(obj1.__dict__)
print(obj1_json)






