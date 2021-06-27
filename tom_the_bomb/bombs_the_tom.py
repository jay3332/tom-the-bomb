from __future__ import annotations
from abc import ABC

from random import choice


class NotTomTheBomb(Exception):
    def __init__(self) -> None:
        super().__init__(choice((
            'It is clear that imposters are present in your interests.',
            'This is unfortunately, not Tom the bomb (the tom bomb the tom (the bomb))',
            'You must like imposters.',
            'Bomb the tom the not the bomb the tom the bomb',
            'For it is obviously affirmed by the public that such "imposters" are much loved by you.',
            'You clearly do not the bomb the tom the bomb.'
        )))


class AbstractAlvin(ABC):
    """Alvin is abstract"""

    def __init__(self) -> None:
        self.__tom_the_bomb__ = True

    @property
    def tom(self) -> AbstractAlvin:
        """:class:`TomConstructor`: Tom"""
        raise NotTomTheBomb() from None  # trolled

    @property
    def the(self) -> AbstractAlvin:
        """:class:`The`: the"""
        raise NotTomTheBomb() from None  # trolled

    @property
    def bomb(self) -> AbstractAlvin:
        """:class:`Bomb`: bomb"""
        raise NotTomTheBomb() from None  # trolled

    Tom = tom
    Bomb = bomb


class TomConstructor(AbstractAlvin):
    """Represents Tom

    Attributes
    ----------
    tom
        You're dumb
    the
        Cool
    bomb
        You're dumb
    """

    def __init__(self) -> None:
        super().__init__()

    @property
    def the(self) -> The:
        return The()


class The(AbstractAlvin):
    """Represents the

    Attributes
    ----------
    tom
        You're dumb
    the
        You're dumb
    bomb
        cool
    """

    def __init__(self) -> None:
        super().__init__()

    @property
    def bomb(self) -> The:
        print('Tom the bomb')
        return The()


Tom = TomConstructor()
