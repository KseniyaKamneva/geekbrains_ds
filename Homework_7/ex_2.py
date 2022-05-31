"""
Created on Mon May 30 14:16:37 2022

@author: Ксения Камнева
"""

from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, param):
        self.param = param
    
    @property
    @abstractmethod
    def fabric_consumption_rate(self):
        raise NotImplementedError()
    
    def __add__(self, other):
        return self.fabric_consumption_rate + other.fabric_consumption_rate


class Coat(Clothes):
    
    @property
    def fabric_consumption_rate(self):
        return round(self.param / 6.5) + 0.5


class Costume(Clothes):
    
    @property
    def fabric_consumption_rate(self):
        return round(self.param * 2 + 0.3) / 100


if __name__ == "__main__":
    coat = Coat(58)
    costume = Costume(240)
    print(coat + costume)
