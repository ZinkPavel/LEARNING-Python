from enum import Enum
from typing import Self


class Namespace:
    def __init__(
        self: Self,
        name: str = None,
        parent: Self = None,
        sibling: Self = None,
        variables: list[str] = None,
    ) -> None:
        self.name = name
        self.parent = parent
        self.sibling = sibling
        self.variables = variables or list()

    def __str__(self):
        string = f"""
{self.name=}
    {self.parent=}
    {self.sibling=}
    {self.variables=}
"""
        return string


class Command(Enum):
    ADD = "add"
    CREATE = "create"
    GET = "get"


class Programm:
    def __init__(
        self: Self,
        namespaces: dict[str:Namespace] = None,
    ):
        self.namespaces = namespaces or dict()
        if not self.namespaces or "global" not in self.namespaces:
            self.namespaces.update(
                {"global": Namespace(name="global", parent=Namespace(name=None))}
            )

    def __str__(self):
        string = "\n--- Start ---"
        for elem in self.namespaces.values():
            string += str(elem)
        return string + "--- Finish ---"

    def execute(self: Self, command: str):
        args = command.split(" ")
        _command = args[0]
        if _command == Command.ADD.value:
            self.__add_variable_to_namespace(*args[1:])
        elif _command == Command.CREATE.value:
            self.__create_new_namespace(*args[1:])
        elif _command == Command.GET.value:
            return self.__get_namespace_containing_var(*args[1:])
        else:
            raise (RuntimeError(f"Command {_command} is not available."))

    def __add_variable_to_namespace(self: Self, namespace: str, variable: str):
        if self.namespaces.get(namespace) is None:
            self.namespaces.update(
                {namespace: Namespace(name=namespace, variables=[variable])}
            )
        else:
            self.namespaces[namespace].variables.append(variable)
        #     raise (RuntimeError(f"Namespace {namespace} is not defined."))

    def __create_new_namespace(self: Self, namespace: str, parent: str):
        _namespace = self.namespaces.get(namespace)
        if _namespace:
            return
            # raise (RuntimeError(f"Namespace {namespace} already exists."))
        new_namespace = Namespace(name=namespace, parent=self.namespaces.get(parent))
        self.namespaces.update({namespace: new_namespace})
        self.namespaces.get(parent).sibling = new_namespace

    def __get_namespace_containing_var(
        self: Self, namespace: Namespace, variable: str
    ) -> str:
        _namespace = self.namespaces.get(namespace)
        if _namespace is None:
            return None
        if variable in _namespace.variables:
            return _namespace.name
        else:
            return self.__get_namespace_containing_var(_namespace.parent.name, variable)


if __name__ == "__main__":
    prog = Programm()
    n = int(input())
    for _ in range(n):
        prog.execute(input())
