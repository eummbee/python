from modules.mylib import food

print(food.name)
food.cook()
food.eat()
print()

from modules.mylib.food import name, cook, eat

print(name)
cook()
eat()
print()

import bbb.cm2
print(bbb.cm2.add(1,2))

import bbb.cm2 as bc
print(bc.add(3,4))