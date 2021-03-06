# -*- coding: utf-8 -*-

from enum import Enum

Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

for name, member in Month.__members__.items():
    print(name, '=>', member, ',', member.value)

print(Month.Jan)

Month1 = Month.Jan
print(Month1)
print(Month['May'])
print(Month.Jun.value)
print(Month(9))