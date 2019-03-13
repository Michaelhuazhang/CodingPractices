# -*- encoding:utf-8 -*-

'''
@Author : ZJH
@Concat : jianhua-zhang@qq.com
@SoftWare : Pycharm
@File  : code3_CatDogQueue.py
@Time : 2019/3/13 15:06
'''
'''
猫狗队，记录猫狗进队的次数时间
出队的时候按照它们各自的次数进行出队
设置一个宠物栈，存放猫狗和它们的次数
'''
class Pet:
    def __init__(self, typeName):
        self.typeName = typeName

    def getPetType(self):
        return self.typeName

class Dog(Pet):
    def __init__(self):
        super(Dog, self).__init__("Dog")

class Cat(Pet):
    def __init__(self):
        super(Pet, self).__init__("Cat")

class PetEnterQueue:
    def __init__(self, pet, count):
        self.pet = pet
        self.count = count

    def getPet(self):
        return self.pet

    def getCount(self):
        return self.count

    def getEnterType(self):
        return self.pet.getPetType()

class CatDogEnqeue:
    def __init__(self):
        self.cats = []
        self.dogs = []
        self.count = 0

    def add(self, pet):
        if pet.getPetType() == "Dog":
            self.count = 1
            self.dogs.append(PetEnterQueue(pet, self.count))
        elif pet.getPetType() == "Cat":
            self.count += 1
            self.cats.append(PetEnterQueue(pet, self.count))
        else:
            raise TypeError("Not Cat or Dog!")

        def isEmpty(self):
            return len(self.dogs) == 0 and len(self.cats) == 0

        def isDogEmpty(self):
            return len(self.dogs) == 0

        def isCatempty(self):
            return len(self.cats) == 0

        def pollAll(self):
            if not self.isDogEmpty() and not self.isCatempty():
                if self.cats[0].getCount() < self.dogs[0].getCount():
                    return self.cats.pop(0).getPet()
                else:
                    return self.dogs.pop(0).getPet()
            elif not self.isDogEmpty():
                return self.dogs.pop(0).getPet()
            elif not self.isCatempty():
                return self.cats.pop(0).getPet()
            else:
                TypeError("The Queue is Empty")

        def pollDog(self):
            if not self.isDogEmpty():
                return self.dogs.pop(0).getPet()
            else:
                raise IndexError("The Dog queue is Empty")

        def pollCat(self):
            if not self.isCatempty():
                return self.cats.pop(0).getPet()
            else:
                raise IndexError("The Cat queue is Empty")
