"""
Examples using OOP in Python3
"""

import abc

#------------------------------------------------------------------------------#
#                              Parent Class                                    #
#------------------------------------------------------------------------------#

#class Item():
class Item(abc.ABC): #abc makes class abstract (Abstract Base Class)

    _count = 0

    def __init__(self, name):
        self.name = name
        self._private_name = "don't access"
        self.__really_private = "can't access"
        Item._count += 1

    @abc.abstractmethod
    def calc_price(self):
        #print("Calculate the price in Item")
        pass

    @classmethod
    def print_count(cls):
        print("This is a class method, I don't know my instance")
        print(cls._count)

    @staticmethod
    def print_date():
        print("This is a static method, I don't know my class or instance")
        print("Today is ...")

#------------------------------------------------------------------------------#
#                               Subclasses                                     #
#------------------------------------------------------------------------------#

class BookItem(Item):

    def __init__(self, author, **kwargs):
        self.author = author
        super().__init__(**kwargs)

    def get_author(self):
        return self.author

    def calc_price(self):
        print("Calculate the price in BookItem")

#------------------------------------------------------------------------------#

class FoodItem(Item):

    def get_exp_date(self):
        return '12-20-18'





#------------------------------------------------------------------------------#
#book_item = Item("Cats")

# print(Item)
# print(book_item)
# print(book_item.name)
# print(book_item._private_name)
# #print(book_item.__really_private)

#book_item.print_count()

#another_item = Item("Pens")

#Item.print_count()

my_book = BookItem(name='Moon', author='Sam')
my_book.print_count()

your_book = BookItem(name='Moon', author='Sam')
your_book.print_count()

print(my_book.name)

my_book.calc_price()

print("")

for i in (your_book, my_book):
    i.print_date()
    i.print_count()
    i.calc_price()
