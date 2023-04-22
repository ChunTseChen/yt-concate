import abc
from abc import ABC, abstractclassmethod


class Step(ABC):
    def __int__(self):
        pass

    @abc.abstractmethod
    def process(self, data, inputs):
        pass


class StepException(Exception):
    pass
