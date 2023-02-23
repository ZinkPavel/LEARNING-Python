import unittest

from .namespaces import Programm


class TestNamespaces(unittest.TestCase):
    def setUp(self):
        self.prog = Programm()

    def test_1(self):
        self.prog.execute("add global a")
        self.prog.execute("create foo global")
        self.prog.execute("add foo b")
        self.prog.execute("create bar foo")
        self.prog.execute("add bar a")

        self.assertEqual(self.prog.namespaces["global"].variables, ["a"])
        self.assertEqual(self.prog.namespaces["foo"].variables, ["b"])
        self.assertEqual(self.prog.namespaces["bar"].variables, ["a"])

    def test_2(self):
        self.prog.execute("add global a")
        self.prog.execute("create foo global")
        self.prog.execute("add foo b")

        self.assertEqual(self.prog.execute("get foo a"), "global")
        self.assertEqual(self.prog.execute("get foo c"), None)

        self.prog.execute("create bar foo")
        self.prog.execute("add bar a")

        self.assertEqual(self.prog.execute("get bar a"), "bar")
        self.assertEqual(self.prog.execute("get bar b"), "foo")


if __name__ == "__main__":
    unittest.main()
