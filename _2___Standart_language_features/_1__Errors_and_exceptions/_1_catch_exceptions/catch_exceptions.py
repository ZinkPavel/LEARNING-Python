try:
    foo()
except AssertionError:
    print("AssertionError")
except ZeroDivisionError as e:
    print("ZeroDivisionError")
except ArithmeticError:
    print("ArithmeticError")
