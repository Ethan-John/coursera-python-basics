from sys import stdin


class Matrix():
    def __init__(self, list):
        self.list = list

    def __str__(self):
        return '\n'.join(' '.join(map(str, row)) for row in self.list)

    def size(self):
        return len(self.list), len(self.list[0])


exec(stdin.read())
