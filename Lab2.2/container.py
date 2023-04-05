import json
import os
import re


class Container:
    user = str()
    storage: set[str] = set()
    file = str()

    def __init__(self, user):
        self.user = user
        self.file = f'./users/{user}.json'
        #self.load

    def add(self, elem):
        self.storage.add(elem)

    def remove(self, elem):
        self.storage.remove(elem)

    def find(self, elem):
        if elem in self.storage:
            return elem
        else:
            print('No such elements')

    def list(self):
        return list(self.storage)

    def greep(self, regex):
        return list(filter(lambda elem: re.match(regex, elem)), self.storage)

    def save(self):
        os.makedirs(os.path.dirname(self.file), exist_ok = True)
        with open(self.file, 'w') as f:
            json.dump(list(self.storage), f)

    def load(self):
        if os.path.exists(self.file):
            with open(self.file, 'r') as f:
                self.storage = set(json.load(f))

    def switch(self, user):
        self.user = user
        self.file = f'./users/{user}.json'
        self.storage.clear()
