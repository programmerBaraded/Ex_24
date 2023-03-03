# В фермерском хозяйстве в Карелии выращивают чернику.
# Она растет на круглой грядке, причем кусты высажены только по окружности.
# Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растет N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло
# различное число ягод – на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники.
# Эта система состоит из управляющего модуля и нескольких собирающих модулей.
# Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом,
# собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход
# собирающий модуль, находясь перед некоторым кустом заданной во входном файле грядки.

import random
some_kust = int(input("Введите количество кустов: "))
plantaciy = [random.randint(1, 50) for _ in range(some_kust)]
print(plantaciy)

max_cherniki = 0

for i in range(len(plantaciy)-1):
    if plantaciy[i - 1] + plantaciy[i] + plantaciy[i + 1] > max_cherniki:
        max_cherniki = plantaciy[i - 1] + plantaciy[i] + plantaciy[i + 1]
    if plantaciy[0] + plantaciy[1] + plantaciy[len(plantaciy) - 1] > max_cherniki:
        max_cherniki = plantaciy[0] + plantaciy[1] + plantaciy[len(plantaciy) - 1]
    if plantaciy[0] + plantaciy[len(plantaciy) - 2] + plantaciy[len(plantaciy) - 1] > max_cherniki:
        max_cherniki = plantaciy[0] + plantaciy[len(plantaciy) - 2] + plantaciy[len(plantaciy) - 1]

print(f"Максимального числа черники, которое может собрать за один заход собирающий модуль {max_cherniki} ягод.")