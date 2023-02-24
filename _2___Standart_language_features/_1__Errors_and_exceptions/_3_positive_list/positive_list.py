class NonPositiveError(Exception):
    ...


class PositiveList(list):
    def append(self, object):
        if object <= 0:
            raise NonPositiveError()
        super().append(object)
