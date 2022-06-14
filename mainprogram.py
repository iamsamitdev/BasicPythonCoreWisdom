# การ import มาทั้งหมด
# import number

# print(number.factorial(5))
# print(number.fibonacci(100))

# การ import มาบางฟังก์ชัน
# from number import factorial, fibonacci
# from number import *

# print(factorial(5))
# print(fibonacci(100))

# การ import พร้อมทั้งชื่อนามแฝง
# from number import factorial as ft, fibonacci as fb

# print(ft(5))
# print(fb(100))

# การ Import จาก Package numberpackage
# from numberpackage import calculate as cl
# from numberpackage import number as nb
# from numberpackage import *
import numberpackage

# print(cl.plus(2,3))
# print(nb.factorial(5))

print(numberpackage.plus(2,3))
print(numberpackage.factorial(5))
print(numberpackage.fibonacci(100))