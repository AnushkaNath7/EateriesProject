from mainapp.models import *


def makeFood():
    file1 = open('file.txt', 'r')
    Lines = file1.readlines()
    for line in Lines:
        items = line.split(";")
        a = Food(name=items[0], price=int(items[1]),
                 restaurant=items[2], type=int(items[3]))
        a.save()
