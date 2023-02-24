class Programm:
    def __init__(self):
        self.classes = dict()

    def add_class(self, name, parents=None):
        self.classes.update({name: Class(name, parents or list())})

    def a_is_subclass_b(self, a, b):
        b = self.classes.get(b)
        if not b:
            return
        if a in b.parents or b.name == a:
            return True
        else:
            for parent in b.parents:
                if self.a_is_subclass_b(a, parent):
                    return True


class Class:
    def __init__(self, name, parents=None):
        self.name = name
        self.parents = parents or list()


if __name__ == "__main__":
    prog = Programm()

    n = int(input())
    for _ in range(n):
        command = input().split(" : ")
        parents = None
        if len(command) > 1:
            parents = command[1].split(" ")
        prog.add_class(command[0], parents=parents)

    result = ""
    q = int(input())
    for _ in range(n):
        a, b = input().split(" ")
        result += f'{"Yes" if prog.a_is_subclass_b(a, b) else "No"}\n'

    print(result)
