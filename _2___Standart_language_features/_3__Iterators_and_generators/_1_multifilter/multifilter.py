class multifilter:
    def judge_half(pos, neg):
        # допускает элемент, если его допускает хотя бы половина фукнций (pos >= neg)
        return pos >= neg

    def judge_any(pos, neg):
        # допускает элемент, если его допускает хотя бы одна функция (pos >= 1)
        return True if pos >= 1 else False

    def judge_all(pos, neg):
        # допускает элемент, если его допускают все функции (neg == 0)
        return pos > 0 and neg == 0

    def __init__(self, iterable, *funcs, judge=judge_any):
        # iterable - исходная последовательность
        self.iterable = iter(iterable)
        # funcs - допускающие функции
        self.funcs = funcs
        # judge - решающая функция
        self.judge = judge

    def __iter__(self):
        # возвращает итератор по результирующей последовательности
        return self

    def __next__(self):
        while True:
            item = next(self.iterable)
            pos, neg = 0, 0
            for func in self.funcs:
                if func(item):
                    pos += 1
                else:
                    neg += 1

            if self.judge(pos, neg):
                return item


# Альтернативный вариант.
# Функция __next__ при этом не нужна.
# Функция __inter__ заменяется.

# def __iter__(self):
#     for item in self.iterable:
#         pos, neg = 0, 0
#         for func in self.funcs:
#             if func(item):
#                 pos += 1
#             else:
#                 neg += 1

#         if self.judge(pos, neg):
#             yield item
