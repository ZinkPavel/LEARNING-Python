def closest_mod_5(x: int) -> int:
    if x % 5 == 0:
        return x
    else:
        return (x + 5) // 5 * 5


# def closest_mod_5(x: int) -> int:
# return x if x % 5 == 0 else closest_mod_5(x + 1)
