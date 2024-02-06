class add:
    a = 10
    b = 10
    c = a+b
    print(c)
ma = add()

class animal:
    def __init__(self,name,color):
        self.name = name
        self.color = color
        print(f'Animal name {self.name}')
        print(f'Animal color {self.color}')
a = animal('Dog','white')

o = open('mahendra.txt')
print(o.read())
