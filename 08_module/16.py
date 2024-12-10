import cal_module

print(cal_module.add(1,2))
print(cal_module.sub(1,2))
print(cal_module.div(1,2))
print(cal_module.mul(1,2))

from cal_module import add #cal_module에 add 만 불러오기
print(add(1,2))
#cal_module.add() -> 안됨!

import cal_module as cm #cal_module 이름을 cm으로 부르겠다
print(cm.add(1,2))

