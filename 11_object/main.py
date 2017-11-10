import os
import sys

class Animal:
    __name = ""
    __height = 0
    __weight = 0
    __sound = 0

    def __init__(self, name,height,weight,sound):
        self.__name = name
        self.__height = height
        self.__weight = weight
        self.__sound = sound

    def set_name(self, name):
        self.__name = name
    def get_name(self):
        return self.__name
    def get_type(self):
        return "Animal"
    def get_sound(self):
        return self.__sound
    def get_height(self):
        return  self.__height
    def get_weight(self):
        return self.__weight
    def toString(self):
        return "{} is {} cm tall and {} k.g. and say {}".format(self.__name,self.__height,self.__weight,self.__sound)


class Dog(Animal):
    __owner = ""
    
    def __init__(self, name,height,weight,sound,owner):
        self.__owner = owner
        super(Dog, self).__init__(name,height,weight,sound)
    
    def set_owner(self,owner):
        self.__owner = owner
    
    def get_owner(self):
        return self.__owner

    def get_type(self):
        print("Dog")

    def toString(self):
        return "{} is {} cm tall and {} k.g. and say {} His owner is {}".format(self.get_name(),self.get_height(),self.get_weight(),self.get_sound(),self.__owner)

    def multiple_sounds(self, how_mane=None):
        if how_mane is None:
            print(self.get_sound())
        else:
            print(self.get_sound() * how_mane)

a = Animal("Dog",60,45,"boc")
print(a.get_name())
print(a.toString())

d = Dog("Boron",30,18,"Hong","Tong")
print(d.toString())
d.multiple_sounds(30)
