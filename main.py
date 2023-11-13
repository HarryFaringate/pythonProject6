i = 1
k = 0
masa = []
#import random
class people:
    name = None
    age = None
    pidor = None

    def set(self, name, age, pidor):
        self.name = name
        self.age = age
        self.pidor = pidor

    def get(self, name, age, pidor):
        self.name = input()
        self.age = input()
        self.pidor = input()

    def vet(self):
        print(self.name, self.age, self.pidor)

print('выебрите действия:','\n','ввести нового человека 1 ','\n','показать информацияю по человеку 2 ','\n','вывести масив 3' )
v = int(input())
if v == 1:
    mas = people()
    r = None
    print('Имя,возраст,пидор ли он')
    mas.get(mas.name, mas.age, mas.pidor)
    masa.extend(mas)
    #r=random.randint(100, 999)
    #masive.write(str(r))
    #masive.close()
    print('Номер человека',mas[0,1,2])
if v ==2:
    r=input()
    for r in mas:
        print(r)
if v ==3:
    print(mas)
cre