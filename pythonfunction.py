# การสร้างฟังก์ชันใน Python
def hello():
    print("Hello Python")


# เรียกใช้งานฟังก์ชัน hello()
hello()


# การสร้างฟังก์ชันแบบมี Argument
def info(msg):
    print("Welcome to", msg)


info("ITGenius")


# การสร้างฟังก์ชันใน Python
def area(width, height):
    return width * height


print(area(10, 20))


def show_info(name = "", salary = 84360, lang = "Python"):
    print(f'Name: {name}')
    print('Salary: %d' % salary)
    print(f'Language: {lang}')
    print()


show_info()
show_info("Samit")
show_info("Wichai", 100000, "Java")


