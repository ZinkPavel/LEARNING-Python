import unittest

from .inheritance_model import Programm


class TestInheritanceModel(unittest.TestCase):
    def setUp(self):
        self.prog = Programm()

    def test_0(self):
        self.prog.add_class("G", ["F"])
        self.prog.add_class("A")
        self.prog.add_class("B", ["A"])
        self.prog.add_class("C", ["A"])
        self.prog.add_class("D", ["B", "C"])
        self.prog.add_class("E", ["D"])
        self.prog.add_class("F", ["D"])
        self.prog.add_class("X")
        self.prog.add_class("Y", ["X", "A"])
        self.prog.add_class("Z", ["X"])
        self.prog.add_class("V", ["Z", "Y"])
        self.prog.add_class("W", ["V"])

        self.assertTrue(self.prog.a_is_subclass_b("A", "G"))
        self.assertFalse(self.prog.a_is_subclass_b("A", "Z"))
        self.assertTrue(self.prog.a_is_subclass_b("A", "W"))
        self.assertTrue(self.prog.a_is_subclass_b("X", "W"))
        self.assertFalse(self.prog.a_is_subclass_b("X", "QWE"))
        self.assertFalse(self.prog.a_is_subclass_b("A", "X"))
        self.assertTrue(self.prog.a_is_subclass_b("X", "X"))
        self.assertFalse(self.prog.a_is_subclass_b("1", "1"))

    def test_1(self):
        self.prog.add_class(
            "classA", ["classB", "classC", "classD", "classG", "classH"]
        )
        self.prog.add_class(
            "classB", ["classC", "classE", "classG", "classH", "classK", "classL"]
        )
        self.prog.add_class(
            "classC", ["classE", "classD", "classH", "classK", "classL"]
        )
        self.prog.add_class("classE", ["classD", "classF", "classK", "classL"])
        self.prog.add_class("classD", ["classG", "classH"])
        self.prog.add_class("classF", ["classK"])
        self.prog.add_class("classG", ["classF"])
        self.prog.add_class("classH", ["classL"])
        self.prog.add_class("classK", ["classH", "classL"])
        self.prog.add_class("classL")

        self.assertTrue(self.prog.a_is_subclass_b("classK", "classD"))
        self.assertTrue(self.prog.a_is_subclass_b("classD", "classA"))
        self.assertTrue(self.prog.a_is_subclass_b("classG", "classD"))
        self.assertTrue(self.prog.a_is_subclass_b("classH", "classA"))
        self.assertTrue(self.prog.a_is_subclass_b("classE", "classE"))
        self.assertTrue(self.prog.a_is_subclass_b("classH", "classG"))
        self.assertFalse(self.prog.a_is_subclass_b("classE", "classL"))
        self.assertFalse(self.prog.a_is_subclass_b("classB", "classD"))
        self.assertFalse(self.prog.a_is_subclass_b("classD", "classL"))
        self.assertFalse(self.prog.a_is_subclass_b("classD", "classG"))
        self.assertTrue(self.prog.a_is_subclass_b("classD", "classE"))
        self.assertFalse(self.prog.a_is_subclass_b("classA", "classF"))
        self.assertFalse(self.prog.a_is_subclass_b("classA", "classC"))
        self.assertTrue(self.prog.a_is_subclass_b("classK", "classA"))
        self.assertFalse(self.prog.a_is_subclass_b("classA", "classH"))
        self.assertTrue(self.prog.a_is_subclass_b("classK", "classD"))
        self.assertTrue(self.prog.a_is_subclass_b("classH", "classB"))
        self.assertTrue(self.prog.a_is_subclass_b("classK", "classB"))
        self.assertFalse(self.prog.a_is_subclass_b("classD", "classL"))
        self.assertTrue(self.prog.a_is_subclass_b("classG", "classG"))
        self.assertFalse(self.prog.a_is_subclass_b("classA", "classH"))
        self.assertFalse(self.prog.a_is_subclass_b("classK", "classL"))
        self.assertTrue(self.prog.a_is_subclass_b("classG", "classE"))
        self.assertTrue(self.prog.a_is_subclass_b("classB", "classA"))
        self.assertFalse(self.prog.a_is_subclass_b("classC", "classK"))
        self.assertFalse(self.prog.a_is_subclass_b("classK", "classL"))
        self.assertFalse(self.prog.a_is_subclass_b("classC", "classL"))
        self.assertTrue(self.prog.a_is_subclass_b("classG", "classC"))
        self.assertTrue(self.prog.a_is_subclass_b("classD", "classD"))
        self.assertFalse(self.prog.a_is_subclass_b("classC", "classG"))
        self.assertTrue(self.prog.a_is_subclass_b("classE", "classA"))
        self.assertFalse(self.prog.a_is_subclass_b("classF", "classK"))
        self.assertFalse(self.prog.a_is_subclass_b("classB", "classG"))
        self.assertFalse(self.prog.a_is_subclass_b("classH", "classL"))
        self.assertTrue(self.prog.a_is_subclass_b("classL", "classF"))
        self.assertTrue(self.prog.a_is_subclass_b("classH", "classG"))
        self.assertTrue(self.prog.a_is_subclass_b("classD", "classA"))
        self.assertFalse(self.prog.a_is_subclass_b("classH", "classL"))
